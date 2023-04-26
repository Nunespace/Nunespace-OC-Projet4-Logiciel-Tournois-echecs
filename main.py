import json
import os
from views.menu import Menu
from views.messages import Messages
from controllers.menu_manager import MenuManager
from controllers.tournament_manager import TournamentManager
from controllers.user_manager import UserManager


def main():
    tournament_manager = TournamentManager()
    user_manager = UserManager()
    menu = Menu()
    messages = Messages()

    if os.path.exists("tournaments_data.json"):
        with open("tournaments_data.json") as file:
            tournaments_data = json.load(file)
    else:
        tournaments_data = []

    run = MenuManager(
        tournament_manager, user_manager, menu, messages, tournaments_data
    )
    run.choice_main_menu()


if __name__ == "__main__":
    main()
