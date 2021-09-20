import requests

def heroes_list():
    url_1 = "https://superheroapi.com/api/2619421814940190/search/Captain America"
    url_2 = "https://superheroapi.com/api/2619421814940190/search/Hulk"
    url_3 = "https://superheroapi.com/api/2619421814940190/search/Thanos"
    response_1 = requests.get(url_1, timeout=5)
    response_2 = requests.get(url_2, timeout=5)
    response_3 = requests.get(url_3, timeout=5)
    captain_america = response_1.json()
    hulks = response_2.json()
    thanos = response_3.json()
    intelligence = []
    list_heroes = []
    for data_heroes in captain_america['results']:
        intelligence.append(data_heroes['powerstats']['intelligence'])
        list_heroes.append(
            {data_heroes['powerstats']['intelligence']: data_heroes['name']}
        )
    for data_heroes_2 in hulks['results']:
        list_heroes.append(
            {data_heroes_2['powerstats']['intelligence']: data_heroes_2['name']}
        )
    for data_heroes_3 in thanos['results']:
        list_heroes.append(
            {data_heroes_3['powerstats']['intelligence']: data_heroes_3['name']}
        )
        intelligence.extend(list_heroes)

    return list_heroes

if __name__ == "__main__":
    max_iq_heroes = 0
    list_heroes = heroes_list()
    for heroes_list in list_heroes:
        for iq_heroes, name_heroes in heroes_list.items():
            iq_heroes = int(iq_heroes)
            if iq_heroes > max_iq_heroes:
                max_iq_heroes = iq_heroes
                max_name_iq_heroes = name_heroes

    print(f'Герой "{max_name_iq_heroes}" является самым умным и имеет интеллект: {max_iq_heroes}')