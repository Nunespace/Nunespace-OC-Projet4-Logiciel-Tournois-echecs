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
        #print("total des points trié:",total_points_sorted)       
        while len(total_points_sorted)>0:
            n = 0
            for players in range(len (total_points_sorted)):
                match = total_points_sorted[n][0], total_points_sorted[n+1][0]
                #print("paire = ",match)
                #print(self.pairCheck(match))
                if not self.pairCheck(match):
                    list_matches.append(match)
                    del total_points_sorted[n:n+2]
                    break
                elif self.pairCheck(match):
                    n+=1            
        #print()
        #print("liste des matchs :", list_matches) 
        #print("total des points trié:",total_points_sorted)
        
        return list_matches
        
        
        

    def pairCheck(self, match) :
        """ Vérifie si les matchs ont déjà été joués lors des tours précédents"""
        for round in range (1, self.round_number) :
            round_name = "round_"+str(self.round_number-1)+"_results"
            for players in self.tournament_data[round_name]:
                #print("players:", players[0][0], players[1][0])
                #print("pair : ", pair[0], pair[1])
                if match[0] == players[0][0] and match[1] == players[1][0]:
                    #print("Ce match a déjà été joué au round", round)
                    return True
                elif match[1] == players[0][0] and match[0] == players[1][0]:
                    #print("Ce match a déjà été joué au round", round,".")
                    return True
                       
                    

        
                        
       
                
                
                


        
tournament_name = "champignons"
place = "Limoges"
starting_date = "23 avril 2023"
end_date = "20 mai 2023"
round_numbers = 4
players_list = [
"BOUILLON Paul",
"CAZENAVE George",
"DURAND Anne",
"MARTIN Jacques",
"ROSE Pierre",
"VANDENABEL Sophie"
]
description = "blabla"

pair = ('DURAND Anne', 'CAZENAVE George')



#round1 = Round(tournament_name, 1, players_list)
#print(round1.matchesRound1())
#print(round2.matchesRoundNext(2))
#round4.pairCheck(pair)













