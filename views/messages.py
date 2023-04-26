class Messages:
    def messages_tournament(self, tournament_name, message_number):
        """Affiche des messages concernant un tournoi"""
        if message_number == 1:
            print()
            print(f'Le tournoi "{tournament_name}" a bien été enregistré.')
        if message_number == 2:
            print("Les paires de tous les tours de ce tournoi ont déjà été générées.")

    def messages_round(self, round_number, message_number):
        """Affiche des messages concernant un round"""
        if message_number == 1:
            print("Les résultats de ce tour ont déjà été saisis.")
        if message_number == 2:
            print(
                "Veuillez saisir les résultats du tour précédent avant de générer les paires."
            )
        if message_number == 3:
            print()
            print(
                f"Tous les résultats du round n°{round_number} ont bien été enregistrés."
            )
            print()
        if message_number == 4:
            print()
            print("Les résultats de tous les tours de ce tournoi ont déjà été saisis.")
        if message_number == 5:
            print(
                f"Vous devez générer les paires du tour n°{round_number} avant de saisir ses résultats."
            )

    def messages_players(self, message_number):
        """
        Affiche des messages concernant l'enregistrement d'un nouveau joueur
        """
        if message_number == 1:
            print("Ce joueur a bien été enregistré.")

    def show_list_matches(self, round_number, list_matches):
        """
        Affiche la liste des matchs après la génération des paires d'un round
        """
        print(f"Les matchs du round n°{round_number} sont les suivants :")
        for i, players in enumerate(list_matches):
            print("Match n°", i + 1, ":", players[0], "vs", players[1])

    def report_players(self, list_players):
        """Affiche le rapport : Liste de tous les joueurs"""
        print("LISTE DE TOUS LES JOUEURS")
        print()
        for player in list_players:
            print(player)

    def report_tournaments(self, list_tournaments):
        """Affiche le rapport : Liste de tous les tournois"""
        print("LISTE DE TOUS LES TOURNOIS")
        print()
        for tournament in list_tournaments:
            print("¤", tournament)

    def report_list_players_tournament(self, tournament):
        """
        Affiche le rapport : Liste des joueurs d'un tournoi
        préalablement sélectionné par l'utilisateur
        """
        list_players_tournament = tournament["players_list"]
        list_players_tournament.sort()
        print(f'LISTE DES JOUEURS DU TOURNOI "{tournament["tournament_name"].upper()}"')
        print()
        for player in list_players_tournament:
            print("¤", player)

    def report_rounds_results_tournament(self, tournament):
        """
        Affiche le rapport : Liste des matchs d'un tournoi
        préalablement sélectionné par l'utilisateur:
        tous les matchs de tous les tours avec, le cas échéant
        les résultats, sont affichés.
        """
        print(
            f'          LISTE DES MATCHS DU TOURNOI "{tournament["tournament_name"].upper()}"'
        )
        print()
        for i in range(tournament["round_numbers"]):
            round_name = "round_" + str(i + 1) + "_results"
            list_round = tournament[round_name]
            round_number = i + 1
            print(f"                        ¤¤TOUR n°{round_number}¤¤           ")
            print()
            print(f"Début : {tournament[round_name][-2][1]}")
            print(f"Fin : {tournament[round_name][-1][1]}")
            del list_round[0]
            del list_round[-2:]
            print(
                "-------------------------------------------------------------------------------"
            )
            for match in list_round:
                print(
                    match[0][0], ":", match[0][1], " vs ", match[1][0], ":", match[1][1]
                )
                print(
                    "-------------------------------------------------------------------------------"
                )
            print()
            print()
        print("TOTAL DES POINTS :")
        total_points_sorted = sorted(
            tournament["total_points"].items(), key=lambda t: t[1]
        )
        for player in total_points_sorted:
            print(f"¤ {player[0]} : {player[1]} points")

    def report_messages(self, message):
        """
        Affiche un message concernant le rapport:
        Liste des matchs d'un tournoi
        """
        if message == 1:
            print(
                "Attention, tous les résultats de ce tournoi n'ont pas été saisis avant de générer ce rapport."
            )
