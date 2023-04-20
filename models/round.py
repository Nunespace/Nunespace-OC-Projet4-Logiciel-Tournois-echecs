import json

from random import randrange
from .tournament import Tournament

class Round(Tournament):
    
    def __init__(self, tournament_data, round_number):
       super().__init__(tournament_data)     
       self.round_number = round_number
               

    def matchesRound1(self):
        """création de la liste des matchs du 1er tour (choix aléatoire) et sauvegarde dans le fichier tournaments_data.json"""
        list_matches = []
        n = 0 
        
        list_players = self.tournament_data["players_list"]
        while n < len(list_players) :
            match = [list_players[n], list_players[n+1]]
            list_matches.append(match)
            n+=2
        return list_matches
        
    def matchesRoundNext(self):
        """Crée la liste des matchs d'un round en fonction du total des points des joueurs. 
        La liste tient compte également des matchs précédents pour éviter que 2 joueurs se rencontrent à nouveau (le nombre de tours étant limité au nombre de joueurs). """     
        list_matches = []      
        total_points_sorted = sorted(self.tournament_data["total_points"].items(), key=lambda t: t[1])

        for i in range (len(total_points_sorted)+1):
            for i in range(len(total_points_sorted)-1):
                print(i)
                player1 = 0
                player2 = i+1
                match = total_points_sorted[player1][0], total_points_sorted[player2][0]               
                if self.pairCheck(match) ==True :
                    list_matches.append(match)
                    del total_points_sorted[player1]
                    del total_points_sorted[player2-1]
                    break
        print(total_points_sorted)
                
                    
        return list_matches
        
       
        
        

    def pairCheck(self, match) :
        """ Vérifie si les matchs ont déjà été joués lors des tours précédents"""  
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
            
                    
               

                       
                    

        
                        
       
                
                
                


        













