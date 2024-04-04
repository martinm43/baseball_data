#!/usr/bin/env python3

## Ben Kite
## 2017-02-16

## Timer and error handling edits by Martin Miller, 2023-04-13
"""
Finds all game played in the year that you specify and saves
their results in a single .csv file.

The output file will be named with the year followed by "Games.csv".

"""

import pandas, os, argparse, time
from baseballReferenceScrape import pullGameData

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--year", help="Year of games to be collected. Eventually I'll allow multiple years (e.g., 2010-2012 or 2010 2012 2013, etc.)")
parser.add_argument("--datdir", help="Name of directory where the data should be stored.  If the directory does not exist it will be created. Defaults to data/", default = "data/")

args = parser.parse_args()

start_time = time.perf_counter()

year  = str(args.year)
directory = str(args.datdir)

def YearData(year, directory):
    year = str(year)

    if not os.path.exists(directory):
        os.makedirs(directory)

    dataBase = dict()

    teams = ['ANA','ATL', 'ARI', 'BAL', 'BOS','CAL', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'FLA',
             'KCR', 'HOU', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'MON', 'NYM', 'NYY', 'OAK',
             'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBD','TBR', 'TEX', 'TOR', 'WSN']

    #Adding in pre-1977 teams.
    #teams.append(['WSA','SEP','KCA','MLN','WSH','BRO','NYG','PHA','SLB','BSN']) --temp fix for 2024 updates.

    for tm in teams:
        gd = pullGameData(tm, year)
        if type(gd) is int:
            if gd == 404:
                print(tm + " not found in database for year "+str(year))
                pass
            if gd == 429:
                print("SR rate limit exceeded. Ending execution now.")
                break
        else: 
            print("Team "+tm+" processed successfully for year "+str(year))
            dataBase[tm] = gd

        #Pause is now required to avoid hitting stricter rate limiting.
        #Proven working value is 5
        #time.sleep(5) 

    #Debug printing
    #for tm in teams:
    #    print(tm)
    #    print(dataBase[tm])
        
    gameData = pandas.concat(dataBase)

    gameData.rename(columns = {"Tm" :"HomeTeam", 
                               "Opp":"AwayTeam", 
                               "Record":"HomeRecord",
                               "Runs":"R", 
                               "OppRuns":"RA",  
                               "W-L":"HomeWL",  
                               "Streak":"HomeStreak"}, inplace = True)
   
    gameData = gameData.sort_values(["Date"])

    #gameData = gameData.drop("gamenum", axis = 1)
    #gameData = gameData.drop("gamenum2", axis = 1)
    #gameData = gameData.drop("boxscore", axis = 1)

    homeData = gameData[gameData["Location"] != "@"]

    homeData = homeData.drop("Location", axis = 1)

    homeData["Index"] = range(0, len(homeData))

    outfile = directory + year + "Games.csv"

    homeData["year"] = year

    homeData.to_csv(outfile, index = False, encoding = "utf-8")
    return(homeData)

## Now the function is defined, use it

YearData(year, directory)

passed_time = time.perf_counter() - start_time
print(f"Obtaining data for {year} took {passed_time/60} min")
