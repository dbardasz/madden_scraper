import requests
import pandas as pd
import os

# change this to the place you want the csvs to save in
directory_files_save = r'C:\Users\dbard\OneDrive\Documents\madden_files'

team_dict = {1: 'Chicago Bears',
             2: 'Cincinnati Bengals',
             3: 'Buffalo Bills',
             4: 'Denver Broncos',
             5: 'Cleveland Browns',
             6: 'Tampa Bay Buccaneers',
             7: 'Arizona Cardinals',
             8: 'Los Angeles Chargers',
             9: 'Kansas City Chiefs',
             10: 'Indianapolis Colts',
             11: 'Dallas Cowboys',
             12: 'Miami Dolphins',
             13: 'Philadelphia Eagles',
             14: 'Atlanta Falcons',
             15: 'San Francisco 49ers',
             16: 'New York Giants',
             17: 'Jacksonville Jaguars',
             18: 'New York Jets',
             19: 'Detroit Lions',
             20: 'Green Bay Packers',
             21: 'Carolina Panthers',
             22: 'New England Patriots',
             23: 'Las Vegas Raiders',
             24: 'Los Angeles Rams',
             25: 'Baltimore Ravens',
             26: 'Washington Football Team',
             27: 'New Orleans Saints',
             28: 'Seattle Seahawks',
             29: 'Pittsburgh Steelers',
             30: 'Tennessee Titans',
             31: 'Minnesota Vikings',
             32: 'Houston Texans'}

for key in team_dict:
    madden_json = requests.get(
        'https://ratings-api.ea.com/v2/entities/m22-ratings?filter=iteration:launch-ratings%20AND%20teamId:({})&sort=overall_rating:DESC,firstName:ASC'.format(
            key))
    api_call = madden_json.json()
    players = api_call.get('docs')
    df = pd.DataFrame(players)
    os.chdir(directory_files_save)
    df.to_csv('{} Madden Ratings.csv'.format(team_dict.get(key)), index=False)