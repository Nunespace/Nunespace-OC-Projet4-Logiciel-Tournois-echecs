import random
from .tournament import Tournament


class Round(Tournament):
    def __init__(self, tournament_data, round_number):
        super().__init__(tournament_data)
        self.round_number = round_number

    def matchesRound1(self):
        """
        création de la liste des matchs du 1er tour (choix aléatoire)
        et sauvegarde dans le fichier tournaments_data.json
        """
        list_matches = []
        n = 0
        tournament_data = self.tournament_data
        list_players = tournament_data["players_list"]
        list_players_shuffle = random.sample(list_players, len(list_players))
        while n < len(list_players_shuffle):
            match = [list_players_shuffle[n], list_players_shuffle[n + 1]]
            list_matches.append(match)
            n += 2
        return list_matches

    def matches_round_next_based_on_points(self):
        """
        La liste des matchs est générée selon
        le total des points de chaque joueur
        Si cette méthode n'aboutit pas alors
        la méthode matches_round_next_based_on_matrix(self) prend le relais
        """
        list_matches = []
        total_points_sorted = sorted(
            self.tournament_data["total_points"].items(), key=lambda t: t[1]
        )
        player1 = 0
        player2 = 1
        n = -1
        while len(total_points_sorted) > 0:
            if player2 <= len(total_points_sorted) - 1:
                if len(total_points_sorted) > 2:
                    match = (
                        total_points_sorted[player1][0],
                        total_points_sorted[player2][0],
                    )
                    if self.pair_check(match):
                        list_matches.append(match)
                        del total_points_sorted[player1]
                        del total_points_sorted[player2 - 1]
                        player1 = 0
                        player2 = 1
                    else:
                        player2 += 1
                elif len(total_points_sorted) == 2:
                    match = total_points_sorted[0][0], total_points_sorted[1][0]
                    if self.pair_check(match):
                        list_matches.append(match)
                        return list_matches
                    else:
                        n += 1
                        list_matches = []
                        total_points_sorted = sorted(
                            self.tournament_data["total_points"].items(),
                            key=lambda t: t[1],
                        )
                        if n <= (len(total_points_sorted) - 2):
                            total_points_sorted[n], total_points_sorted[n + 1] = (
                                total_points_sorted[n + 1],
                                total_points_sorted[n],
                            )
                        else:
                            list_matches = self.matches_round_next_based_on_matrix()
                            return list_matches
            else:
                list_matches = self.matches_round_next_based_on_matrix()
                return list_matches
        return list_matches

    def matches_round_next_based_on_matrix(self):
        """
        Si la méthode matches_round_next_based_on_points(self)
        ne donne pas de résultat, alors cette fonction est activée:
        la liste des matchs est générée selon la matrice des matchs,
        c'est à dire selon les paires déjà jouées.
        """
        matrix_matches = self.tournament_data["matrix_matches"]
        total_players = len(self.tournament_data["players_list"])
        # création d'une liste à mélanger composée de numéros,
        # chaque numéro correspond à un joueur
        list_to_shuffle = []
        for i in range(total_players):
            list_to_shuffle.append(i)
        total_round_matches = int(total_players / 2)
        list_matches_numbers_ok = []
        # la liste des matchs est vidée avant chaque remaniement jusqu'à
        # ce qu'une combinaison de paires corresponde à des matchs non joués
        while len(list_matches_numbers_ok) != total_round_matches:
            list_matches_numbers_ok = []
            # la liste est mélangée
            random.shuffle(list_to_shuffle)
            n = 0
            list_matches_numbers = []
            # à partir de la liste mélangée, création d'une liste de paires
            for i in range(0, total_round_matches):
                match = list_to_shuffle[n], list_to_shuffle[n + 1]
                n += 2
                list_matches_numbers.append(match)
            # la liste des matchs est comparée à la matrice des matchs :
            # si le match n'a pas été déjà joué, il est ajouté
            #  à la liste des matchs possibles
            for match in list_matches_numbers:
                player1 = match[0]
                player2 = match[1]
                if matrix_matches[player1][player2] == 0:
                    list_matches_numbers_ok.append(match)
        # à partir de la liste précédente, création de la liste des matchs
        #  du round (list_matches) avec le nom et prénom des joueurs
        players_number = self.number_allocation_to_players()
        list_matches = []
        for pair in list_matches_numbers_ok:
            for number in players_number:
                if pair[0] == number[0]:
                    player1 = number[1]
                if pair[1] == number[0]:
                    player2 = number[1]
            list_matches.append((player1, player2))
        return list_matches

    def pair_check(self, match):
        """
        Vérifie si un match a déjà été joué lors des tours précédent.
        Retourne True si le match n'a jamais été joué.
        """
        for round in range(1, self.round_number):
            round_name = "round_" + str(round) + "_results"
            for players in self.tournament_data[round_name]:
                if match[0] == players[0][0] and match[1] == players[1][0]:
                    return False
                elif match[1] == players[0][0] and match[0] == players[1][0]:
                    return False
        return True

    def matrix_matches(self, list_matches):
        """
        Attribution d'un numéro à chaque joueur
        (de 0 au nombre total de joueur -1)
        """
        matrix = self.tournament_data["matrix_matches"]
        players_number = self.number_allocation_to_players()
        for match in list_matches:
            for player in players_number:
                if match[0] == player[1]:
                    index1 = player[0]
                if match[1] == player[1]:
                    index2 = player[0]
            matrix[index1][index2] = 1
            matrix[index2][index1] = 1
        return matrix

    def number_allocation_to_players(self):
        players_number = []
        for i, player in enumerate(self.tournament_data["players_list"]):
            players_number.append((i, player))
        return players_number
