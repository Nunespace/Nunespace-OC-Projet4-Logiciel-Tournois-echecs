import json
import platform
import os



class Menu:
    
    def main_menu(self):
        print()
        print ("****Menu principal****")
        print()
        while True:
            menu_options = {
            1: "Tournois",
            2: "Joueurs",
            3: "Rapports",
            4: "Fermer"
            }
            for key in menu_options:
                print (key, '--', menu_options[key] )
                print()
            option = int(input('Entrer votre choix : '))
            for key in menu_options:
                if option == key:
                    self.clean()
                    return option
            print()        
            print("Option invalide. Merci d'entrer un nombre entre 1 et 4")

 
    def tournament_menu(self):
        print()
        print ("*****Menu Tournoi*****")
        print()
        while True:
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
            option = int(input('Entrer votre choix : '))
            for key in menu_options:
                if option == key:
                    self.clean()
                    return option
            print()
            print("Option invalide. Merci d'entrer un nombre entre 1 et 5")



    def reports_menu(self):
        pass


    def choice_tournaments(self):
        with open('tournaments_data.json') as file:
            tournaments_data = json.load(file)
        print ("Liste des tournois : ")
        print()
        tournaments_list=[]
        for tournament in tournaments_data:
            tournaments_list.append(tournament["tournament_name"])
        for i, tournament in enumerate(tournaments_list) :
            print (i+1, ":", tournament)
        print()
        tournament_chosen = int(input("Veuillez entrer le numéro du tournoi : "))
        print()
        for tournament in tournaments_data:
            if tournament["tournament_name"] == tournaments_list[tournament_chosen-1] :
                return tournament
    
    def clean(self):
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
   
    


       
           
        

        
        
        

    




  

    


