###
### Author: Xin Li.
### Description: In this short PA, I will be writing
### a program that reads in a game log file. My
### program will process the information, and then
### print out a summary. This program should both read
### from a file.
### Program name: summarizer.py
###
def main():
    file_name = input('enter gamelog file name:\n')
    team_1 = 0 #team total score
    team_2 = 0 #team total score
    count_players = 0 #total players
    first = '' #first score player
    last = 'Warren' #last score player

    file = open(file_name,'r')
    new_file = open('summary', 'w')
    lines = file.readlines()

    count_players=0

    summary_name = [] #name list
    name_team=[] #name of team
    team_name1='' # name of specific team
    team_name=[]
    name_goal=[]

    team_1_namme, team_2_namme = team_name0(lines, name_team)
    team_1, team_2, count_players,first,last=function_1(lines,name_goal,team_name,team_1_namme,team_2_namme,summary_name,count_players,team_1,team_2)
    if team_1 > team_2:
        print(team_1_namme,'won!')

    if team_1 == team_2:
        print(' No one won!')

    if team_1 < team_2:
        print(team_2_namme, 'won!')

    print(team_1_namme,'scored', team_1, 'points.')

    print(team_2_namme,'scored', team_2, 'points.')

    print(count_players, 'players scored.')

    print(first, 'scored first.')

    print(last,'scored last.')
def team_name0(lines,name_team):
    for i in range(len(lines)):
        team_name1=''
        for index in range(len(lines[i])):
            if lines[i][index]==' ':
                break
            else:
                team_name1+=lines[i][index]
        if team_name1 not in name_team:
            name_team.append(team_name1)
    return name_team[0], name_team[1]

def function_1(lines,name_goal,team_name,team_1_namme,team_2_namme,summary_name,count_players,team_1,team_2):
    for line in lines:
        line = line.split(' ')
        if line[0] not in team_name:
            team_name.append(line[0])
        if line[0]==team_1_namme:
            team_1 += int(line[2])
        if line[0]==team_2_namme:
            team_2 += int(line[2])
        name = line[1]
        name_goal.append(name)
        if name not in summary_name :
            summary_name.append(line[1])
            count_players += 1
    first = name_goal[0]
    last = name_goal[len(name_goal)-1]
    return team_1, team_2, count_players,first,last
main()
