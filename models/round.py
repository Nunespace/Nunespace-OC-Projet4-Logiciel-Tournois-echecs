import json
import time
import random
from .tournament import Tournament

class Round(Tournament):
    
    def __init__(self, tournament_data, round_number):
       super().__init__(tournament_data)     
       self.round_number = round_number
               

    def matchesRound1(self):
        """création de la liste des matchs du 1er tour (choix aléatoire) et sauvegarde dans le fichier tournaments_data.json"""
        list_matches = []
        n = 0 
        tournament_data=self.tournament_data
        list_players = tournament_data["players_list"]
        list_players_shuffle = random.sample(list_players, len(list_players))
        while n < len(list_players_shuffle) :
            match = [list_players_shuffle[n], list_players_shuffle[n+1]]
            list_matches.append(match)
            n+=2  
        return list_matches

    def matches_round_next_based_on_points(self):
        list_matches = []      
        total_points_sorted = sorted(self.tournament_data["total_points"].items(), key=lambda t: t[1])
        player1 = 0
        player2 = 1
        n=-1
        while len(total_points_sorted)>0 :
            print("player1, player2 :", player1, player2)
            print(total_points_sorted)
            #time.sleep(3)
            if player2 <= len(total_points_sorted)-1:
                if len(total_points_sorted)>2:
                    match = total_points_sorted[player1][0], total_points_sorted[player2][0]
                    if self.pair_check(match) ==True :
                        list_matches.append(match)
                        del total_points_sorted[player1]
                        del total_points_sorted[player2-1]
                        player1 = 0
                        player2 = 1
                    else :
                        player2 +=1
                elif len(total_points_sorted) == 2:
                    print("coucou?")
                    match = total_points_sorted[0][0], total_points_sorted[1][0]
                    if self.pair_check(match) ==True :
                        list_matches.append(match)
                        return list_matches
                    else:
                        n+=1
                        print("n",n)
                        list_matches=[]
                        total_points_sorted = sorted(self.tournament_data["total_points"].items(), key=lambda t: t[1])
                        print((len(total_points_sorted)-1))
                        if n <= (len(total_points_sorted)-2):
                            total_points_sorted[n], total_points_sorted[n+1] =  total_points_sorted[n+1], total_points_sorted[n]
                        else:
                            list_matches = self.matches_round_next_based_on_matrix()
                            return list_matches
            else:
                list_matches = self.matches_round_next_based_on_matrix()
                return list_matches
        return list_matches
                
    def matches_round_next_based_on_matrix(self):
        matrix_matches = self.tournament_data["matrix_matches"]
        total_players= len(self.tournament_data[ "players_list"])
        # liste de tous les matchs non réalisés 
        possibles_matches = []
        for ligne in matrix_matches:
            print(ligne)
        for ligne in range(total_players):
            for colonne in range(total_players):
                if matrix_matches[ligne][colonne] == 0:
                    match = ligne, colonne
                    possibles_matches.append(match)
        print("possibles_matches",possibles_matches)
        #création d'une liste à partir des matchs où chaque joeur n'est présent qu'une fois
        list_matches_not_separated = []
        n=0
        for pair in possibles_matches:
            possibles_matches.remove((pair[1],pair[0]))
        print ("possibles_matches nettoyé", possibles_matches)
                                    
        while len(list_matches_not_separated )!=len(possibles_matches):
            for pair in possibles_matches:
                if list_matches_not_separated ==[]:
                    list_matches_not_separated.append(pair[0])
                    list_matches_not_separated.append(pair[1])
                else:
                    if pair[0] not in list_matches_not_separated  and pair[1] not in list_matches_not_separated :
                        list_matches_not_separated.append(pair[0])
                        list_matches_not_separated.append(pair[1])
            print("list_matches_not_separated", list_matches_not_separated)
            list_matches_not_separated_len = len(list_matches_not_separated)
            numbers_of_matches = total_players/2
            time.sleep(3)
            if list_matches_not_separated_len != numbers_of_matches and n< len(possibles_matches)-1:
                n+=1
                print("nn", n)
                list_matches_not_separated  = []
                print("possibles match: ", possibles_matches)
                list_matches_not_separated.append(possibles_matches[n][0])
                list_matches_not_separated.append(possibles_matches[n][1])
                print ("list_matches_not_separated aprèsn+=1", list_matches_not_separated)
                for pair in possibles_matches:
                    if pair[0] not in list_matches_not_separated  and pair[1] not in list_matches_not_separated :
                        list_matches_not_separated.append(pair[0])
                        list_matches_not_separated.append(pair[1])
            # à partir de la liste précédente, création des paires des matchs du round avec numéro des joueurs
            pairs_numbers=[]
            for i in range (int(len(list_matches_not_separated)/2)):
                pairs_numbers.append((list_matches_not_separated[0], list_matches_not_separated[1]))
                del list_matches_not_separated [0:2]
            players_number = self.number_allocation_to_players()
            list_matches=[]
            print("pairs_numbers",pairs_numbers)
            for pair in pairs_numbers:
                for number in players_number:
                    if pair[0]==number[0]:
                        player1 = number[1]
                        print("player1", player1)
                    if pair[1]==number[0]:
                        player2 = number[1]
                        print("player2",player2)
                list_matches.append((player1, player2))
            print("list des matchs:", list_matches)
            return list_matches


    def pair_check(self, match) :
        """Vérifie si les matchs ont déjà été joués lors des tours précédent"""
        for round in range (1, self.round_number) :
            round_name = "round_"+str(round)+"_results"
            for players in self.tournament_data[round_name]:
                if match[0] == players[0][0] and match[1] == players[1][0]:
                    print(f"Ce match a déjà été joué au round{round}")
                    return False
                elif match[1] == players[0][0] and match[0] == players[1][0]:
                    print(f"Ce match a déjà été joué au round {round}.")
                    return False
        return True
    
    def matrix_matches(self, list_matches):
        matrix = self.tournament_data["matrix_matches"]
        print(matrix)
        players_number = self.number_allocation_to_players()
        for match in list_matches:
            for player in players_number:
                if match[0] == player[1] :
                    index1 = player[0]
                if match[1]== player[1]:
                    index2= player[0]
            matrix[index1][index2]=1
            matrix[index2][index1]=1
        return matrix
 
    def number_allocation_to_players(self):
        players_number = []
        for i, player in enumerate(self.tournament_data["players_list"]) :
            players_number.append((i, player))
        return players_number



            
                    
               

                       
                    

        
                        
       
                
                
                


        













