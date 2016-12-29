## 3. The Math Module ##

import math
a = math.sqrt(16)
b= math.ceil(111.3)
c = math.floor(89.9)

## 4. Variables Within Modules ##

import math

print(math.pi)
a = math.sqrt(math.pi)
b  = math.ceil(math.pi)
c = math.floor(math.pi)

## 5. The CSV Module ##

import csv
nfl = list(csv.reader(open('nfl.csv')))

## 6. Counting How Many Times a Team Won ##

import csv
nfl = list(csv.reader(open('nfl.csv')))
patriots_wins = 0
for item in nfl:
    if 'New England Patriots'== item[2]:
        patriots_wins += 1

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(data,teamname):
    wins = 0
    for item in data:
        if teamname == item[2]:
            wins +=1
    return(wins)
cowboys_wins = nfl_wins(nfl,'Dallas Cowboys')
falcons_wins = nfl_wins(nfl,'Atlanta Falcons')

## 10. Working with Boolean Operators ##

a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = a < 5 or b > a

# a < 5 and b > a
result3 = a < 5 and b > a

# a == 5 or b == 5
result4 = a == 5 or b == 5

# a > b or a == 10
result5 = a > b or a == 10

## 11. Counting Wins in a Given Year ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count = count + 1
    return count
def nfl_wins_in_a_year(data,team,year):
    wins = 0
    for item in data:
        if (item[2] == team and item[0] == year):
            wins +=1
    return(wins)
browns_2010_wins = nfl_wins_in_a_year(nfl,'Cleveland Browns','2010')
eagles_2011_wins = nfl_wins_in_a_year(nfl,'Philadelphia Eagles','2011')