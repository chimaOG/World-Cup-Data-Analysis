'''
We need two data sets for this project. 
This particular notebook will be for wrandling and cleaning the data.
Other notebooks will be used for the data visualisation parts of the project

The data is gotten from the FIFA world cup archives and is quite clean so there isn't a lot of cleaning to do
'''

#################################################
#The first data set is high level world cup data from 1930 to 2014
#################################################

#Importing Libraries
import pandas as pd

#import CSV file and drop unnecessary columnns

world_cups = pd.read_csv('WorldCups.csv')
world_cups = world_cups.drop(columns = ['Country','Runners-Up', 'Third', 'Fourth', 'MatchesPlayed', 'Attendance'])

#replace Germany FR with Germany
world_cups = world_cups.replace('Germany FR','Germany')

#################################################
#The first data set is data of world cup matches from 1930 to 2014
#################################################

#import excel file, select the required columnns and group the data by teams

matches_import = pd.read_excel('world-cup-data.xlsx')
matches_import = matches_import.replace('FRG', 'Germany')
matches = matches_import[['attendance','team', 'goals']].groupby(['team']).sum()
