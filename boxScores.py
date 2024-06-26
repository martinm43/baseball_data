#!/usr/bin/env python3

## Modifications by Martin Miller
## 2023-05-19

## Ben Kite
## 2017-02-16

"""Pulls all boxscores for a team for a single season.  Requires user to provide the team and the year.

The teams are indicated by providing one of the following abreviations:
['ATL', 'ARI', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 
 'KCR', 'HOU', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 
 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']

This can take up to six minutes to run for a single team!  I'm going
to work toward this having an update option so that data can be
scraped during the course of a season and quickly added to a .csv
file.

Running the following would give you all boxscores for the Yankees in 2010:

$ python boxScores.py --team NYY --year 2010

"""
import time
import argparse
import baseballReferenceScrape as ds

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--team", help="Name of team from which you want to collect data.")
parser.add_argument("--year", help="Year of games to be collected")
parser.add_argument("--datdir", help="Directory to save output", default = "data/")
args = parser.parse_args()

start_time = time.perf_counter()

year  = str(args.year)
team = str(args.team)
datdir = str(args.datdir)
        
ds.pullBoxscores(team, year, datdir, overwrite = True)
    
passed_time = time.perf_counter() - start_time
print(f"Obtaining data took {passed_time/60} min")