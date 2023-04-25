import json
from models.players import Players
from views.menu import Menu
from views.messages import Messages
from views.datas import PromptForDatas


class UserManager:
    def __init__(self):
        self.menu = Menu()
        self.messages = Messages()
        self.datas = PromptForDatas()

    def report_generation_list_players(self):
        """Génération du rapport : Liste des joueurs"""
        with open("players_data.json") as file:
            players_data = json.load(file)
        list_players = []
        for player in players_data:
            list_players.append(player["first_name"] + " " + player["name"])
        list_players.sort()
        return list_players

    def report_generation_list_tournaments(self):
        """Génération du rapport : Liste des tournois"""
        with open("tournaments_data.json") as file:
            tournaments_data = json.load(file)
        list_tournaments = []
        for tournament in tournaments_data:
            list_tournaments.append(tournament["tournament_name"])
        list_tournaments.sort()
        return list_tournaments

    def players(self):
        """
        Traitement de l'enregistrement de nouveaux joueurs
        dans le fichier des joueurs players_data.json
        """
        players = Players()
        dict_player = self.datas.prompt_for_new_players(players.players_data)
        if dict_player is None:
            return None
        else:
            new_player = Players()
            new_player.update_players_data(dict_player)
            self.messages.messages_players(1)
            self.players()
