import json
import os


class Tournament:
    def __init__(self, tournament_data) :
        self.tournament_data = tournament_data
        self.tournament_name = tournament_data["tournament_name"]
        self.place =  tournament_data["place"]
        self.starting_date = tournament_data["starting_date"]
        self.end_date = tournament_data["end_date"]
        self.players_list = tournament_data["players_list"]
        self.description = tournament_data["description"]
        self.round_numbers = tournament_data["round_numbers"]
             

    def saveData_tournament(self):
        """
        enregistre les données du tournoi (dictionnaire) dans le fichier des tournois : tournament_data.json
        """
        if os.path.exists('tournaments_data.json'):
            with open('tournaments_data.json') as file:
                tournaments_data = json.load(file)
                #print("def save_data_tournament:", tournaments_data)
                tournaments_data.append(self.tournament_data)
                #print(self.tournament_data())
            with open('tournaments_data.json', 'w', encoding='utf-8') as f_out:
                json.dump(tournaments_data, f_out, indent=1)
        else:
            tournaments_data = [self.tournament_data]       
        with open('tournaments_data.json', 'w', encoding='utf-8') as f_out:
            json.dump(tournaments_data, f_out, indent=1)
        
        
               


