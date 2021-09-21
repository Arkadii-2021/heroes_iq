import requests

names_heroes_list = ['Captain America', 'Hulk', 'Thanos']
url = 'https://superheroapi.com/api/2619421814940190/search/'
url_heroes_list = []
for heroes in names_heroes_list:
    url_heroes_list.append(url + heroes)

list_heroes = []

def heroes_list(url_s):
    for url in url_s:
        response_url = requests.get(url, timeout=5)
        response = response_url.json()
        for data_heroes in response['results']:
            list_heroes.append(
                {data_heroes['powerstats']['intelligence']: data_heroes['name']}
            )
    return list_heroes


if __name__ == "__main__":
    max_iq_heroes = 0
    list_heroes = heroes_list(url_heroes_list)
    for heroes_list in list_heroes:
        for iq_heroes, name_heroes in heroes_list.items():
            iq_heroes = int(iq_heroes)
            if iq_heroes > max_iq_heroes:
                max_iq_heroes = iq_heroes
                max_name_iq_heroes = name_heroes

    print(f'Герой "{max_name_iq_heroes}" является самым умным и имеет интеллект: {max_iq_heroes}')
