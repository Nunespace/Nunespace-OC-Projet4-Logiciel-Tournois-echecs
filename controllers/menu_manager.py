import json


class MenuManager:
    def __init__(
        self, tournament_manager, user_manager, menu, messages, tournaments_data
    ):
        self.tournament_manager = tournament_manager
        self.user_manager = user_manager
        self.menu = menu
        self.messages = messages
        self.tournaments_data = tournaments_data

    def choice_main_menu(self):
        """
        Activation des méthodes selon le choix de l'utilisateur
        au menu principal
        """
        self.menu.clean()
        option = self.menu.main_menu()
        if option == 1:
            self.choice_menu_tournament()
        elif option == 2:
            self.user_manager.players()
            self.choice_main_menu()
        elif option == 3:
            self.choice_menu_reports()
        elif option == 4:
            exit()

    def choice_menu_tournament(self):
        """
        Activation des méthodes selon le choix de l'utilisateur
        au menu Tournois
        """
        option = self.menu.tournament_menu()
        if option == 1:
            self.tournament_manager.get_data_tournament()
            self.choice_menu_tournament()
        elif option == 2:
            tournament_data = self.menu.choice_tournaments()
            with open("tournaments_data.json") as file:
                tournaments_data = json.load(file)
            for tournament in tournaments_data:
                if tournament == tournament_data:
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

    def choice_menu_reports(self):
        """
        Activation des méthodes selon le choix de l'utilisateur
        au menu Rapports
        """
        option = self.menu.choice_report()
        if option == 1:
            list_players = self.user_manager.report_generation_list_players()
            self.messages.report_players(list_players)
            self.choice_menu_reports()
        elif option == 2:
            list_tournaments = self.user_manager.report_generation_list_tournaments()
            self.messages.report_tournaments(list_tournaments)
            self.choice_menu_reports()
        elif option == 3:
            tournament_data = self.menu.choice_tournaments()
            with open("tournaments_data.json") as file:
                tournaments_data = json.load(file)
            for tournament in tournaments_data:
                if tournament == tournament_data:
                    self.choice_submenu_report_tournament(tournament)
        elif option == 4:
            self.menu.clean()
            self.choice_main_menu()
        elif option == 5:
            return exit()

    def choice_submenu_report_tournament(self, tournament):
        """
        Activation des méthodes selon le choix de l'utilisateur
        au sous_menu Rapports
        """
        option = self.menu.choice_report_tournament(tournament)
        if option == 1:
            self.messages.report_list_players_tournament(tournament)
            self.choice_submenu_report_tournament(tournament)
        elif option == 2:
            try:
                self.messages.report_rounds_results_tournament(tournament)
            except KeyError:
                self.messages.report_messages(1)
                self.choice_menu_tournament()
            else:
                self.choice_submenu_report_tournament(tournament)
        elif option == 3:
            self.menu.clean()
            self.choice_main_menu()
        elif option == 4:
            return exit()
