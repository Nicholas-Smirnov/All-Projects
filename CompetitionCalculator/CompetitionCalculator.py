#╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭╮
#┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╭╯╰┳╯╰╮╱╱╱╱╱╱╱┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃┃╱╱╭╯╰╮
#┃┃╱╰╋━━┳╮╭┳━━┳━┻╮╭╋╮╭╋┳━━┳━╮╱┃┃╱╰╋━━┫┃╭━━┳╮╭┫┃╭━┻╮╭╋━━┳━╮
#┃┃╱╭┫╭╮┃╰╯┃╭╮┃┃━┫┃┣┫┃┣┫╭╮┃╭╮╮┃┃╱╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃┃┃╭╮┃╭╯
#┃╰━╯┃╰╯┃┃┃┃╰╯┃┃━┫╰┫┃╰┫┃╰╯┃┃┃┃┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰┫╰╯┃┃
#╰━━━┻━━┻┻┻┫╭━┻━━┻━┻┻━┻┻━━┻╯╰╯╰━━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━┻━━┻╯
#╱╱╱╱╱╱╱╱╱╱┃┃
#╱╱╱╱╱╱╱╱╱╱╰╯

#Usage

#We are creating a teams dictionary.
#This will give us the information needed.

#Note, you need to have the tabulate module downloaded.
#If not, type this into your terminal.
#pip install tabulate
from tabulate import tabulate

#This is a dictionary of all of the teams.
Teams = {
    
    #This is Team #1's folder/dictionary.
    'Team #1': {
        
        #These are the medal placements of Team #1.
        'Points': [
            14,
            14,
            8
        ],
        
    },
    
    #You can create as many teams as you want.
    
    'Team #2': {
        
        'Points': [
            1,
            2,
            1
        ],
        
    },
    
    'Team #3': {
        
        'Points': [
            2,
            5,
            6
        ],
        
    },
    
    'Team #4': {
        
        'Points': [
            3,
            2,
            6
        ],
        
    },
    
    'Team #5': {
        
        'Points': [
            5,
            10,
            1
        ],
        
    },
    
}

#The parameters will show what types of statistics you want.
Parameters = {
    
    #This will show you the average of all points.
    "Average": True,
    
    #This will show you the sum of all the points.
    "Sum": True,
    
    
}

#Sort is if you want to sort the teams by best score to worse.
Sort = True

#This is the code that will sort the teams based on their points.
def SortList(OurList):
    l = len(OurList)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (float(OurList[j][1]) > float(OurList[j + 1][1])):
                tempo = OurList[j]
                OurList[j]= OurList[j + 1]
                OurList[j + 1]= tempo
    
    return OurList

#This will just calculate the average.
def Average(Stats):
    return sum(Stats) / len(Stats)

#This is where the results will be calculated.
def CalculateResults(Teams, Parameters, Sort):
    
    #Getting all dictionary keys to use later.
    AllTeams = Teams.keys()
    CurrentParameters = Parameters.keys()

    FinalTeamsStats = [] 

    #Creating the header based on the keys.    
    TemporaryList = ["Team Name"]
    
    for Parameter in CurrentParameters:
        if Parameters[Parameter] == True:
            TemporaryList.append(Parameter)
    
    FinalTeamsStats.append(TemporaryList)
    
    #Creating a counter just to index the keys.
    Counter = 0
    
    for SingleTeam in AllTeams:
        FinalTeamsStats.append([SingleTeam])
        
        Counter = Counter + 1
        
        Team = Teams[SingleTeam]
    
        #If average is true then:
        if Parameters["Average"] == True:
            TeamAverage = Average(Teams[SingleTeam]["Points"])
            FinalTeamsStats[Counter].append(round(TeamAverage, 2))
    
        #If sum is true then:
        if Parameters["Sum"] == True:
            TeamSum = sum(Teams[SingleTeam]["Points"])
            FinalTeamsStats[Counter].append(TeamSum)
          
    #Sorting our code if true.
    if Sort == True:
        
        TemporaryList = ["Team Name"]
        
        for Parameter in CurrentParameters:
            if Parameters[Parameter] == True:
                TemporaryList.append(Parameter)
             
        FinalTeamsStats1 = []
        FinalTeamsStats1.append(FinalTeamsStats[0])
        FinalTeamsStats1.extend(SortList(FinalTeamsStats[1:]))
        
           
    FinalFinalTeamsStats = []
    
    
    # FinalFinalTeamsStats.append(TemporaryList)

    if Sort == True:
        x = FinalTeamsStats1
    else:
        x = FinalTeamsStats
        
    for i in x:
        FinalFinalTeamsStats.append(i)
    
    return FinalFinalTeamsStats

#This is where we create our table.
def FormatTable(AllStats):
    return tabulate(AllStats, tablefmt='fancy_grid', showindex = True)

#Running our function.
Stats = CalculateResults(Teams, Parameters, Sort)

#Printing our table.
print(FormatTable(Stats))

#Coded by Nicholas Smirnov
