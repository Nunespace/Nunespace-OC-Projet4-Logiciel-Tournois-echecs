

class Messages:

    def messages_tournament(self, tournament_name, message_number):
        if message_number == 1:
            print(f'Le tournoi "{tournament_name}" a bien été enregistré.')

    def messages_round(self, round_number, message_number):
        if message_number == 1:
            print ("Les résultats de ce tour ont déjà été saisis.")
        if message_number == 2:
            print ("Veuillez saisir les résultats du tour précédent avant de générer les paires")
        if message_number == 3:
            print (f"Tous les résultats du round n°{round_number} ont bien été enregistrés.")
        if message_number == 4:
            print (f"Les paires de tous les tours de ce tournoi ont déjà été générées.")
        if message_number == 5:
            print (f"Les résultats de tous les tours de ce tournoi ont déjà été saisis.")
        
        
        if message_number == 7:
            print(f"Vous devez générer les paires du tour n°{round_number} avant de saisir les résultats.")



    def messages_players(self, message_number):
        if message_number == 1:
            print ("Ce joueur a bien été enregistré.")

    def show_list_matches(self, round_number, list_matches):
        print (f"les matchs du round n°{round_number} sont les suivants :")
        for i, players in enumerate(list_matches) :
            print ("Match n°", i+1, ":", players[0], "vs", players[1])