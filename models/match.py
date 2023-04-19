import json
from random import randrange
from .round import Round

class Match(Round):
    def __init__(self, tournament_data, round_number, round_name, match_number, result):
        super().__init__(tournament_data, round_number)   
        self.round_name = round_name
        self.match_number = match_number
        self.result = result

    def match_result(self):
        tournament_data = self.tournament_data
        round_name = self.round_name
        match_number = self.match_number
        result = self.result
        player1 = tournament_data[round_name][match_number][0][0]
        player2 = tournament_data[round_name][match_number][1][0]
        if result == 0:
            tournament_data[round_name][match_number][0][1]=1
            tournament_data[round_name][match_number][1][1]=0
            tournament_data["total_points"][player1]+=1
        elif result == 1:
            tournament_data[round_name][match_number][1][1]=1
            tournament_data[round_name][match_number][0][1]=0
            tournament_data["total_points"][player2]+=1
        else:
            tournament_data[round_name][match_number][1][1]=0.5
            tournament_data[round_name][match_number][0][1]=0.5      
            tournament_data["total_points"][player1]+=0.5
            tournament_data["total_points"][player2]+=0.5      
        return tournament_data
            




