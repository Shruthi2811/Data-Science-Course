## 2. Introduction to the Data ##

import csv
nfl_suspensions = list(csv.reader(open('nfl_suspensions_data.csv','r')))[1:]
#nfl_suspensions = [item[1:] for item in nfl_suspensions]
years = {}
for item in nfl_suspensions:
    if item[5] in years:
        years[item[5]] +=1
    else:
        years[item[5]] = 1
print(years)        

## 3. Unique Values ##

unique_teams,unique_games= [],[]
for item in nfl_suspensions:
    unique_teams.append(item[1])
    unique_games.append(item[2])
unique_teams = set(unique_teams)   
unique_games = set(unique_games)
print(unique_teams)
print(unique_games)

## 4. Suspension Class ##

class Suspension():
    def __init__(self,data):
        self.name = data[0]
        self.team = data[1]
        self.games = data[2]
        self.year = data[5]
print(nfl_suspensions[2])
third_suspension  = Suspension(nfl_suspensions[2])


## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()