import json
import os


class Players:

    def __init__(self):
        if os.path.exists('players_data.json'):
            with open('players_data.json') as file:
                self.players_data = json.load(file)
        else:
            self.players_data = []
        

    def update_players_data(self, dict_player):
        if os.path.exists('players_data.json'):
            with open('players_data.json') as file:
                players_data = json.load(file)
            players_data.append(dict_player)
            with open('players_data.json', 'w', encoding='utf-8') as f_out:
                json.dump(players_data, f_out, indent=1)
        else:
            with open('players_data.json', 'w', encoding='utf-8') as f_out:
                json.dump([dict_player], f_out, indent=1)

    """
    def list_players_first_name_name(self):
        players_data = self.players_data
        list_players = []
        for player in players_data:
            list_players.append(player["first_name"] + " "+ player["name"])
        list_players.sort()
        return list_players
    """

    def list_players_from_login(self, list_login):
        players_data = self.players_data
        list_players_registered = []
        for login in list_login:
            for player in players_data:
                if login == player["login"]:
                    list_players_registered.append(player["first_name"] + " "+ player["name"])
        return list_players_registered





         





