import json
from views.menu import Menu
from models.players import Players 

#from.menus.menu import.menu
#from.menus.menu import Messages


class MenuManager:
    def __init__(self, tournament_manager, menu, messages, tournaments_data):
        self.tournament_manager = tournament_manager
        self.menu = menu
        self.messages = messages
        self.tournaments_data = tournaments_data
        self.players = Players()
        
    def choice_main_menu(self):
        option = self.menu.main_menu()
        if option == 1:
             self.choice_menu_tournament()
        elif option == 2:
            return self.players()
        elif option == 3:
            return self.reports_menu()
        elif option == 4:
            return exit()

    def choice_menu_tournament(self):
        option = self.menu.tournament_menu()
        if option == 1:
            self.tournament_manager.get_data_tournament()
            self.choice_menu_tournament()
        elif option == 2:
            tournament_data = self.menu.choice_tournaments()
            #round_number = self.menu.choice_round(tournament_name)
            with open('tournaments_data.json') as file:
                tournaments_data = json.load(file)
            for tournament in tournaments_data:
                if tournament == tournament_data:  
                    print(tournament_data)
                    self.tournament_manager.pair_generation(tournament_data)
            self.choice_menu_tournament()          
        elif option == 3:
            tournament_data = self.menu.choice_tournaments()
            self.tournament_manager.get_and_save_results(tournament_data)
            self.choice_menu_tournament()
        elif option == 4:
            self.menu.clean()
            return self.choice_main_menu()
        elif option == 5:
            return exit()
        

    
    


    

