import json
import platform
import os
import time


class Menu:
    
    def main_menu(self):
        
        print()
        while True:
            menu_options = {
            1: "Tournois",
            2: "Joueurs",
            3: "Rapports",
            4: "Fermer"
            }
            print ("****Menu principal****")
            print()
            for key in menu_options:
                print (key, '--', menu_options[key] )
                print()
            try:
                option = int(input('Entrer votre choix : '))
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 4.")
                time.sleep(2)
                self.clean()
                print()  
            else:
                for key in menu_options:
                    if option == key:
                        self.clean()
                        return option      
                print("Option invalide. Merci d'entrer un nombre entre 1 et 4")
                time.sleep(2)
                self.clean()
                print()  

 
    def tournament_menu(self):
        
        while True:
            print()
            print ("*****Menu Tournoi*****")
            print()
            menu_options = {
            1 : "Créer un tournoi",
            2 : "Générer les paires",
            3 : "Saisir les résultats d'un tour",
            4 : "Retour au menu principal",
            5 : "Fermer"
            }
            for key in menu_options:
                print (key, '--', menu_options[key] )
                print()
            try:
                option = int(input('Entrer votre choix : '))
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 5.")
                time.sleep(2)
                self.clean()
                print()
            else:
                for key in menu_options:
                    if option == key:
                        self.clean()
                        return option
                print()
                print("Option invalide. Merci d'entrer un nombre entre 1 et 5")
                time.sleep(2)
                self.clean()
                print()  



    def choice_report(self):      
        while True:
            print()
            print ("*****Menu Rapports*****")
            print()
            menu_options = {
            1 : "Liste des joueurs",
            2 : "Liste des tournois",
            3 : "Afficher les informations d'un tournoi",
            4 : "Retour au menu principal",
            5 : "Fermer"
            }
            for key in menu_options:
                print (key, '--', menu_options[key] )
                print()
            try:

                option = int(input('Entrer votre choix : '))
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 5.")
                time.sleep(2)
                self.clean()
                print()
            else:
                for key in menu_options:
                    if option == key:
                        self.clean()
                        return option
                print()
                print("Option invalide. Merci d'entrer un nombre entre 1 et 5")
                time.sleep(2)
                self.clean()
                print()  

    def choice_report_tournament(self, tournament):
        tournament_name = tournament["tournament_name"]
        
        while True:
            print()
            print (f"****Rapports du tournoi {tournament_name}****")
            print()
            print ("Date de début :", tournament["starting_date"])
            print ("Date de fin :", tournament["end_date"])
            print(f'Nombre de tours : {tournament["round_numbers"]}')
            print()
            print ("Veuillez choisir le type de rapport : ")
            print()
            menu_options = {
            1 : "Liste des joueurs du tournoi",
            2 : "Liste des matchs",
            3 : "Retour au menu principal",
            4 : "Fermer"
            }
            for key in menu_options:
                print (key, '--', menu_options[key] )
                print()
            try:
                option = int(input('Entrer votre choix : '))
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 4.")
                time.sleep(2)
                self.clean()
                print()
            else:
                for key in menu_options:
                    if option == key:
                        self.clean()
                        return option
                print()
                print("Option invalide. Merci d'entrer un nombre entre 1 et 4")
                time.sleep(2)
                self.clean()
                print() 


    def choice_tournaments(self):
        with open('tournaments_data.json') as file:
            tournaments_data = json.load(file)
        while True:
            print ("Liste des tournois : ")
            print()
            tournaments_list=[]
            for tournament in tournaments_data:
                tournaments_list.append(tournament["tournament_name"])
            for i, tournament in enumerate(tournaments_list) :
                print (i+1, ":", tournament)
            print()
            try:
                tournament_chosen = int(input("Veuillez entrer le numéro du tournoi : "))
                print()
            except ValueError:
                print("Vous devez taper un nombre.")
                time.sleep(2)
                self.clean()
                print()
            else :
                for tournament in tournaments_data:
                    if tournament["tournament_name"] == tournaments_list[tournament_chosen-1] :
                        self.clean()
                        return tournament
    
    def clean(self):
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
   
    


       
           
        

        
        
        

    




  

    


