# baseball_data, Martin's fork
This library is forked from the original, with the original description retained below for posterity, for the purposes of keeping this library current for the end user and any other users who might desire to use this library.

## Summary of Changes
Added historical abbreviations for teams so that the repository can take data from previous seasons.

Added a sleep delay to the gameData.py script that tries to take in entire years so that it doesn't trip the SR rate delay.

### Summary of Scripts and their Status - May 17, 2023.

**baseballReferenceScrape.py**
Contains queries used to read BR data.

**battingOverTime.py**
To be tested

**boxScores.py**
To be tested

**gameData.py**
Script obtains an entire year of game data, is used to obtain the data for a current year as well. Is also
coupled with a bash script to process multiple years at once. Works correctly.

**playerData.py**
Obtains data on a player level for an entire season for every team. Works correctly.

**WAR.py**
Calculates expected WAR for a season. To be tested.

**WPA_pitching.py**
To be tested.

**WPA.py**
To be tested.

### To Do: 
Test how timed wait works with other scripts.
Incorporate 429 detection logic/formalize it for other scripts.


 
# baseball_data

Ben Kite

2017-04-11

This directory contains baseballReferenceScrape.py which pulls data
from baseball-reference.com. There are also numerous other scripts
that use the functions defined in baseballReferenceScrape.py to
automate the scraping and stacking of multiple tables.

This collection of scripts was written in Python 3.5.
The scripts are dependent on the following packages:
- pandas
- os
- re
- requests
- bs4
- numpy
- argparse
- matplotlib
- sklearn
- scipy
- statsmodels
- pylab

If you are new to Python, I recommend installing the Anaconda distribution:
- https://www.continuum.io/downloads

baseballReferenceScrape.py:
Contains a series of functions that use bs4.BeautifulSoup to scrape
data from html and put them in pandas data frames.  This is where I
keep all of my data scraping functions.  I will work on adding
comments explaining what is being done with the webpages. All other
scripts in this repo are simply examples and extensions of the
functions in this script.

gameData.py:
I wanted a dataset for a given year that has basic information for all
games played (teams involved, scores, winner, loser, save, attendence,
etc.). I use the “pullGameData” function in baseballReferenceScrape.py
to pull out the data from each teams page for the year I want.  These
datasets have all of the 162 (more if theres postseason play) for that
team.  I stacked all 30 datasets together, removed the duplicate games
(I only used the home games from each team’s page), cleaned up the
variable names to make a bit more sense, and then save the final
product in a .csv file.  This is designed to be run in a console.

playerData.py:
Pull data summarizing individual seasons for players.  This script
pulls data on batting and pitching from 5 different tables that are
found on a teams page of a given year.  See the help info ($ python
playerData.py --help) for instructions.

boxScores.py:
This pulls out box score information for individuals games for a team
for an entire season. It first looks at the team page to see when the
games were, and then it uses those dates to pull individual box
scores. It will take a few minutes to run. See the help info ($ python
boxScores.py --help) for instructions.

battingOverTime.py:
Uses the box score data to create plots to show how players batting
ability changes over the course of the season. This now runs from the
command line.

WPA.py:
Uses play-by-play data to examine wWPA across all batters in the
season specified in the script. Generates tables in .png files
summarizing the top and bottom 30 players in MLB.
