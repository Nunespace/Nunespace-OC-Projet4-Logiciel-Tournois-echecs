from models.players import Players
from.menu_manager import MenuManager


class UserManager(MenuManager):
    
    def reports_generation(self):
        pass
    
    
    def players(self):
        players = Players()
        dict_player = self.view.prompt_for_new_players(players.players_data)
        if dict_player == None:
            self.choice_main_menu()
        else :
            new_player = Players()
            new_player.update_players_data(dict_player)
            self.messages.messages_players(1)
            self.players()
    