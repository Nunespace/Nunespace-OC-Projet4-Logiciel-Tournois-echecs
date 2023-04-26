import json
import datetime

from views.datas import PromptForDatas
from views.messages import Messages
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.players import Players


class TournamentManager:
    def __init__(self):
        self.prompt_for_datas = PromptForDatas()
        self.message = Messages()

    def get_data_tournament(self):
        """
        Traitement des input de l'utilisateur concernant
        la création d'un tournoi : crée un dictionnaire
        et le sauvegarde dans le fichier json tournaments_data.json
        """
        players = Players()
        tournament_data = self.prompt_for_datas.prompt_for_data_tournament(
            players.players_data
        )
        list_players = players.list_players_from_login(tournament_data["players_list"])
        tournament_data["players_list"] = list_players
        dict_total_points = {}.fromkeys(tournament_data["players_list"], 0)
        tournament_data.update([("total_points", dict_total_points)])
        # initialisation de la matrice des matchs
        players_numbers = len(tournament_data["players_list"])
        matrix_matches = [[0] * players_numbers for i in range(players_numbers)]
        for ligne in range(players_numbers):
            # Dans la matrice, quand le joueur est face à lui-même,
            # H est indiqué (comme himself)
            for colonne in range(players_numbers):
                if ligne == colonne:
                    matrix_matches[ligne][colonne] = "H"
                    matrix_matches[colonne][ligne] = "H"
        tournament_data.update([("matrix_matches", matrix_matches)])
        tournoi = Tournament(tournament_data)
        tournoi.saveData_tournament()
        self.message.messages_tournament(tournament_data["tournament_name"], 1)
        if self.prompt_for_datas.prompt_for_list_match_round1():
            self.pair_generation(tournoi.tournament_data)

    def get_and_save_results(self, tournament_data):
        """
        Traitement des input de l'utilisateur concernant
        la saisi des résultats des matchs d'un round :
        met à jour le dictionnaire du tournoi choisi par l'utilisateur
        et le sauvegarde dans le fichier json tournaments_data.json
        """
        n = 0
        # 1ère boucle pour vérifier si les résultats des matchs de chaque tour
        # ont été saisis : s'arrête si non et donne le n°(i) du round à saisir
        for i in range(1, tournament_data["round_numbers"] + 1):
            round_name = "round_" + str(i) + "_results"
            if round_name in tournament_data:
                if tournament_data[round_name][0][1] == 0:
                    round_number = i
                    break
                else:
                    n += 1
            # si les résultats du tour précédent ont été saisis et si le tour n'est pas enregistré,
            # l'utilisateur est invité à le générer
            else:
                round_number = i
                self.message.messages_round(round_number, 5)
                return True
        # si n = nombre de tours, une message indique que tous les résultats
        # ont été saisis puis retourne True
        if n == tournament_data["round_numbers"]:
            self.message.messages_round(i, 4)
            return True
        else:
            round_name = "round_" + str(round_number) + "_results"
            # 2ème boucle pour vérifier quels matchs ont été complétés,
            # s'arrête dès qu'un match n'a pas de résultats
            for j in range(1, len(tournament_data[round_name]) + 1):
                if tournament_data[round_name][j][0][1] == "":
                    match_number = j
                    result = self.prompt_for_datas.prompt_from_results(
                        tournament_data, round_number, match_number
                    )
                    break
        match = Match(tournament_data, round_number, round_name, match_number, result)
        tournament_data = match.match_result()
        tournaments_data = self.load_data()
        # les résultats du match sont enregistrés dans le dict tournament_data
        for tournament in tournaments_data:
            if tournament["tournament_name"] == tournament_data["tournament_name"]:
                tournament["total_points"] = tournament_data["total_points"]
                tournament[round_name] = tournament_data[round_name]
        # vérifie si le dernier match a été complété : si oui,
        # le dictionnaire du tournoi est sauvegardé dans le fichier json
        #  et retrourne True. Si non, sauvegarde le dictionnaire
        ultimate_match = tournament_data[round_name][-3]
        if ultimate_match[0][1] != "":
            tournament_data[round_name][0][1] = 1
            tour_end = datetime.datetime.today().strftime("%Y-%m-%d")
            tournament_data[round_name][len(tournament_data[round_name]) - 1][
                1
            ] = tour_end
            self.message.messages_round(round_number, 3)
            self.saveData(tournaments_data)
            return True
            # self.menu_manager.choice_menu_tournament()
        else:
            self.saveData(tournaments_data)
        # la méthode est de nouveau lancée si le dernier match
        # n'a pas été complété
        self.get_and_save_results(tournament_data)

    def pair_generation(self, tournament_data):
        """
        Traitement des input de l'utilisateur concernant la génération
        des paires pour un round : met à jour le dictionnaire du tournoi
        concerné (choisi par l'utilisateur) et le sauvegarde dans le fichier
        json tournaments_data.json.
        Cette méthode appelle la méthode suivante:
        save_list_matches(self, tournament_data, round_number)
        """
        for i in range(1, tournament_data["round_numbers"] + 1):
            round_name = "round_" + str(i) + "_results"
            if round_name not in tournament_data:
                round_number = i
                return self.save_list_matches(tournament_data, round_number)
        return self.message.messages_tournament(tournament_data["tournament_name"], 2)

    def save_list_matches(self, tournament_data, round_number):
        """
        Suite à la génération des paires, la liste des matchs est
        enregistré dans le dictionnaire du tournoi.
        Ce dernier est sauvegardé dan le fichier tournaments_data.json.
        """
        round = Round(tournament_data, round_number)
        if round_number == 1:
            list_matches = round.matchesRound1()
        else:
            last_round_name = "round_" + str(round_number - 1) + "_results"
            if tournament_data[last_round_name][0][1] == 1:
                list_matches = round.matches_round_next_based_on_points()
            else:
                return self.message.messages_round(round_number, 2)
        matrix_matches = round.matrix_matches(list_matches)
        tournaments_data = self.load_data()
        round_name = "round_" + str(round_number) + "_results"
        round_results = []
        for pair in list_matches:
            round_results.append(([pair[0], ""], [pair[1], ""]))
            # insertion de "Results, 0" pour signifier que les résultats n'ont
            # pas été saisis (0 : pas saisis, 1 : saisis)
        round_results.insert(0, ["Results entered", 0])
        tour_start = datetime.datetime.today().strftime("%Y-%m-%d")
        round_results.insert(len(round_results), ["tour_start : ", tour_start])
        round_results.insert(
            len(round_results), ["tour_end : ", "En attente des resultats"]
        )
        for tournament in tournaments_data:
            if tournament["tournament_name"] == tournament_data["tournament_name"]:
                tournament.update([(round_name, round_results)])
                tournament["matrix_matches"] = matrix_matches
        show_matches = Messages()
        show_matches.show_list_matches(round_number, list_matches)
        self.saveData(tournaments_data)

    def load_data(self):
        """Fonction utile pour éviter la répétition de lignes de code"""
        with open("tournaments_data.json") as file:
            data = json.load(file)
        return data

    def saveData(self, data):
        """Fonction utile pour éviter la répétition de lignes de code"""
        with open("tournaments_data.json", "w", encoding="utf-8") as f_out:
            json.dump(data, f_out, indent=1)
