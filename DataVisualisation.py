# -*- coding: utf-8 -*-
"""
This python file will be used to create the visuals for the project.

The data has been imported and wrangled in the DataPreparation file and we'll import it into this file

The visuals will be created using matplotlib an
d will answer the following question:
1. Which country and continent are the football kings?
2. Which countries have the highest attendance and number of goals scored in world cup histpry?
3. Has the number of goals increased over time and is it primarily because the number of teams have increased?
"""

#Import variables
from DataPreparation import matches, world_cups


#####################  QUESTION 1 VISUALS ######################
#Count how many times each country has won the world cup
num_wins = world_cups['Winner'].value_counts()

#Define a color list for the plot before creating the plot. 
color_list1 = ['r','b','b','r','r','b','b','b']
num_wins.plot(title = 'World Cup Winners', kind = 'bar', color = color_list1)


#####################  QUESTION 2 VISUALS ######################
#select the 25 teams with the most goals and create a plot with the dataframe
goals = matches[['goals']].sort_values(by = 'goals', ascending = False)
goals = goals.iloc[:15, :]
goals.plot(kind = 'bar')

#select the 25 teams with the highest attendance and create a plot with the dataframe
attendance = matches[['attendance']].sort_values(by = 'attendance', ascending = False)
attendance = attendance.iloc[:15, :]
attendance.plot(kind = 'bar')

#####################  QUESTION 3 VISUALS ######################
#Plot the number of goals per world cup over time
goal_scored = world_cups[['Year', 'GoalsScored']]
goal_scored.plot(x = 'Year', y = 'GoalsScored')

#Normalize the data in the goals scored and number of teams columns so we can plot  them on the same graph
goalVSteams = world_cups[['Year', 'GoalsScored','QualifiedTeams']]

dataNorm = ((goalVSteams-goalVSteams.min())/(goalVSteams.max()-goalVSteams.min()))*20
dataNorm["Year"] = goalVSteams["Year"]

dataNorm.plot(x = 'Year', y = ['GoalsScored','QualifiedTeams'])

