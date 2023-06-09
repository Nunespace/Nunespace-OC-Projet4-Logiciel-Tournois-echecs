import time
from .menu import Menu


class PromptForDatas:
    def prompt_for_players(self, players_data):
        """
        Demande à l'utilisateur de saisir l'identifiant de chaque joueur
        participant à un tournoi (pendant la phase de création du tournoi)
        et retourne la liste des identifiants (login).La méthode suivante:
        check_login(self, players_data, login) est utilisée à chaque saisie
        afin de vérifier si le joueur est bien enregistré
        dans le fichier des joueurs players_data.json
        """
        try:
            players_numbers = int(input("Tapez le nombre de joueurs :"))
        except ValueError:
            print("Veuillez taper un nombre.")
            self.prompt_for_players(players_data)
        else:
            if players_numbers % 2 != 0:
                print("Veuillez taper un nombre pair.")
                self.prompt_for_players(players_data)
            else:
                print("Entrez l'identifiant de chaque joueur : ")
                login_list = []
                n = 0
                while n != players_numbers:
                    login = input(f"N° d'identifiant du joueur {n+1} : ")
                    if login in login_list:
                        print(
                            "Ce joueur est déjà inscrit à ce tournoi. Veuillez taper un autre identifiant."
                        )
                    elif self.check_login(players_data, login):
                        login_list.append(login.upper())
                        n += 1
                    else:
                        print(
                            "Cet identifiant n'est pas enregistré dans le fichier des joueurs."
                            "Veuillez taper un autre identifiant."
                        )
            return login_list

    def check_login(self, players_data, login):
        """
        Méthode utilisée par la méthode précédente prompt_for_players
        (self, players_data) : vérifie si l'identifiant (login) correspond
        bien à un joueur présent dans le fichier des joueurs players_data.json
        """
        for player in players_data:
            if player["login"] == login:
                check = 1
                break
            else:
                check = 0
        if check == 1:
            return True
        else:
            return False

    def prompt_for_new_players(self, players_data):
        """
        Demande à l'utilisateur de saisir, ou pas, les données
        d'un nouveau joueur et retourne un dictionnaire contenant ces données
        """
        choice_new_player_yes_no = input(
            "Voulez-vous enregistrer un nouveau joueur? O/N : "
        )
        if choice_new_player_yes_no == "o" or choice_new_player_yes_no == "O":
            menu = Menu()
            menu.clean()
            print("Veuillez saisir les informations suivantes : ")
            dict_player = {}
            dict_player["first_name"] = input("Nom : ").upper()
            dict_player["name"] = input("Prénom :").capitalize()
            dict_player["birthdate"] = input("Date de naissance (JJ/MM/ANNEE):")
            dict_player["login"] = input("Identifiant : ").upper()
            for player in players_data:
                if player["login"] == dict_player["login"]:
                    print("Cet identifiant est déjà utilisé")
                    dict_player["login"] = input("Identifiant : ").upper()
            return dict_player
        else:
            return None

    def prompt_for_data_tournament(self, players_data):
        """
        Demande à l'utilisateur les données d'un tournoi
        lors de sa phase de création et retourne un dictionnaire
        contenant ces données
        """
        tournament_data_dict = {}.fromkeys(
            [
                "tournament_name",
                "place",
                "starting_date",
                "end_date",
                "round_numbers",
                "players_list",
                "description",
            ],
            "",
        )
        print("Veuillez taper les informations suivantes :")
        tournament_data_dict["tournament_name"] = input("Nom du tournoi:")
        tournament_data_dict["place"] = input("Lieu : ")
        tournament_data_dict["starting_date"] = input("date de début (JJ/MM/ANNEE):")
        tournament_data_dict["end_date"] = input("date de fin (JJ/MM/ANNEE):")
        tournament_data_dict["players_list"] = self.prompt_for_players(players_data)
        tournament_data_dict["description"] = input(
            "Veuillez taper une description pour les remarques générales du directeur du tournoi : "
        )
        round_numbers_yes_no = input(
            "Voulez-vous définir le nombre de tours (attention : ce nombre doit être inférieur au nombre de joueurs)"
            ": O/N?"
        )
        print("choix :", round_numbers_yes_no)
        if round_numbers_yes_no == "n" or round_numbers_yes_no == "N":
            tournament_data_dict["round_numbers"] = 4
            if (
                len(tournament_data_dict["players_list"])
                > tournament_data_dict["round_numbers"]
            ):
                return tournament_data_dict
            else:
                print(
                    "Le nombre de joueurs doit être supérieur au nombre de tours  (par défaut : 4 tours)."
                )
                tournament_data_dict["round_numbers"] = int(
                    input(
                        "Veuillez saisir un nombre de round supérieur au nombre de joueurs inscrits : "
                    )
                )
                return tournament_data_dict
        elif round_numbers_yes_no == "o" or round_numbers_yes_no == "O":
            tournament_data_dict["round_numbers"] = int(input("nombre de tours : "))
            while tournament_data_dict["round_numbers"] >= len(
                tournament_data_dict["players_list"]
            ):
                print(
                    "Ce nombre de tour n'est pas inférieur au nombre de joueurs inscrits..."
                )
                tournament_data_dict["round_numbers"] = int(input("nombre de tours : "))
            return tournament_data_dict
        else:
            print("Veuillez taper O pour oui ou N pour non")

    def prompt_for_list_match_round1(self):
        """
        Après l'enregistrement d'un nouveau tournoi,
        l'utiisateur est invité à générer la liste des matchs du 1er tour.
        """
        choice_round_yes_no = input(
            "Voulez-vous générer la liste des matchs du 1er round? O/N :  "
        )
        if choice_round_yes_no == "O" or choice_round_yes_no == "o":
            return True
        else:
            return False

    def prompt_from_results(self, tournament_data, round_number, match_number):
        """Demande à l'utilisateur de saisir les résultats d'un match.
        Retourne None si nul, 0 si le joueur1 gagne, 1 si le joueur2 gagne"""
        round_name = "round_" + str(round_number) + "_results"
        while True:
            print()
            print(f"Match n°{match_number} du round{round_number} :")
            print()
            print("Joueur n°1 :", tournament_data[round_name][match_number][0][0])
            print("VS")
            print("Joueur n°2 :", tournament_data[round_name][match_number][1][0])
            try:
                print()
                result = int(
                    input("Taper le numéro du gagnant ou 0 en cas de match nul : ")
                )
            except ValueError:
                print("Veuillez taper un nombre")
                time.sleep(2)
                print()
            else:
                if result > 2 or result < 0:
                    print(
                        "Veuillez taper le n°du gagnant (1 ou 2) ou 0 en cas de match nul"
                    )
                    time.sleep(2)
                    print()
                elif result == 0:
                    return None
                else:
                    return result - 1
