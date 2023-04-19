from .menu import Menu


class PromptForDatas:

    def prompt_for_players(self, players_data):        
        players_numbers = int(input("Tapez le nombre de joueurs :"))
        print("Entrez l'identifiant de chaque joueur : ")
        login_list = []
        n=1
        while True:
            for nb in range(n, players_numbers+1):
                login = input(f"N° d'identifiant du joueur {nb} : ")
                for player in players_data:
                    print("player login:", player["login"])
                    print("login:", login)
                    if player["login"] == login:
                        login_list.append(login.upper())
                        n+=1
                        break
            return login_list                  
            print("Ce joueur n'est pas enregistré. Veuillez l'enregistrer au préalable via le menu principal ou choisir un autre joueur.")
            
    
    def prompt_for_new_players(self, players_data):
        choice_new_player_yes_no = input("Voulez-vous enregistrer un nouveau joueur? O/N : ")
        if choice_new_player_yes_no == "o" or choice_new_player_yes_no == "O":
            print("Veuillez saisir les informations suivantes : ")
            dict_player = {}
            dict_player["first_name"] = input("Nom : ").upper()
            dict_player["name"] = input("Prénom :").capitalize()
            dict_player["birthdate"] = input("Date de naissance (JJ/MM/ANNEE):")
            dict_player["login"] = input("Identifiant : ").upper()
            for player in players_data:
                if player["login"] == dict_player["login"]:
                    print ("Cet identifiant est déjà utilisé")
                    dict_player["login"] = input("Identifiant : ").upper()
            return dict_player
        else :
            return None



    def prompt_for_data_tournament(self, players_data):
        tournament_data_dict = {}.fromkeys(["tournament_name", "place", "starting_date", "end_date", "round_numbers", "players_list", "description"], "")
        print ("Veuillez taper les informations suivantes :")
        tournament_data_dict["tournament_name"] = input("Nom du tournoi:")
        tournament_data_dict["place"] = input("Lieu : ")
        tournament_data_dict["starting_date"] = input ("date de début (JJ/MM/ANNEE):")
        tournament_data_dict["end_date"] = input ("date de fin (JJ/MM/ANNEE):")
        tournament_data_dict["players_list"] = self.prompt_for_players(players_data)
        tournament_data_dict["description"] = input(f"Veuillez taper une description pour les remarques générales du directeur du tournoi {tournament_data_dict['tournament_name']} : ")
        round_numbers_yes_no = input ("Voulez-vous définir le nombre de tours (attention : ce nombre doit être inférieur au nombre de joueurs) : O/N?")
        # EXCEPT
        print("choix :", round_numbers_yes_no)      
        if round_numbers_yes_no == "n" or round_numbers_yes_no == "N":
            tournament_data_dict["round_numbers"] = 4
            if len(tournament_data_dict["players_list"])> tournament_data_dict["round_numbers"]:
                print("Les données du tournoi ont bien été enregistrées.")
                return tournament_data_dict
            else :
                print("Le nombre de joueurs doit être supérieur au nombre de tours  (par défaut : 4 tours).")
                tournament_data_dict["round_numbers"] = int(input("Veuillez saisir un nombre de round supérieur au nombre de joueurs inscrits : "))
                return tournament_data_dict

        elif round_numbers_yes_no == "o" or round_numbers_yes_no == "O":
            tournament_data_dict["round_numbers"] = int(input("nombre de tours : "))
            while tournament_data_dict["round_numbers"] >= len(tournament_data_dict["players_list"]):
                print("Ce nombre de tour n'est pas inférieur au nombre de joueurs inscrits...")
                tournament_data_dict["round_numbers"]  = int(input("nombre de tours : "))
            print("Les données du tournoi ont bien été enregistrées.")
            return tournament_data_dict
        else:
            print("Veuillez taper O pour oui ou N pour non")
        
        
    def prompt_for_list_match_round1(self):
        choice_round_yes_no = input("Voulez-vous générer la liste des matchs du 1er round? O/N :  ")
        if choice_round_yes_no == "O" or choice_round_yes_no == "o":
            return True
        else :
            return False

          
    def prompt_from_results(self, tournament_data, round_number, match_number):
        tournament_name = tournament_data["tournament_name"]
        menu = Menu()
        menu.clean()
        round_name = "round_"+str(round_number)+"_results" 
        print(f"Match n°{match_number} du round{round_number} :")
        print()
        print ("Joueur n°1 :", tournament_data[round_name][match_number][0][0])
        print ("VS")
        print ("Joueur n°2 :", tournament_data[round_name][match_number][1][0])
        result = int(input("Taper le numéro du gagnant ou 0 en cas de match nul : "))
        if result == 0:
            return None
        else:
            return result-1
    