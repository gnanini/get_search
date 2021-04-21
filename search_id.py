import requests
import json


def search_id(game_name):
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    text = json.loads(response.text)
    id_list = []

    for game in text['applist']['apps']:
        if game_name.lower() in game['name'].lower():
            id_list.append(str(game['appid']) + ' ' + str(game['name']))
        #print(game) #['name'])
        #print(type(game))

    print(id_list)
    return id_list


def test():
    search_id(input('Game name: '))
    return


test()
