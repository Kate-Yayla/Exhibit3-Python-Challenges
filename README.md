# Python Homework #

**PyBank** 

Terminal view:

 

Text view:

 

Visual Studio Code:

import os
import csv

csvpath = os.path.join("..","Resources", "budget_data.csv")
Financialanalysis=os.path.join("Analysis","anaylsis.txt")

#list of variables
totalmonths = 0
totalnet = 0
monthofchange = []
netchangelist = []
greatestincrease = ["",0]
greatestdecrease = ["",0]


with open(csvpath ) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #our data has header, read the header first
    csv_header = next(csvreader)
    #print(f"CSV header:{csv_header}")

    #do not include first row for the net change
    first_row = next(csvreader)
    totalmonths = totalmonths + 1
    totalnet = totalnet + int(first_row[1])
    previousnet = int(first_row[1])

    for row in csvreader:

        #The total number of months included in the dataset 
        # The net total amount of "Profit/Losses" over the entire period
        totalmonths = totalmonths + 1
        totalnet = totalnet + int(row[1])
            #print(total_months)
            #print(total_net)

        
        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        netchange = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchangelist = netchangelist + [netchange]
        monthofchange = monthofchange + [row[0]]
            #print(monthofchange)
        
        #Average
        netmonthlyaverage = sum(netchangelist) / len(netchangelist) 

        # The greatest increase in profits (date and amount) over the entire period
        if netchange > greatestincrease[1]:
           greatestincrease[0] = row[0]
           greatestincrease[1] = netchange
        #  The greatest decrease in profits (date and amount) over the entire period
        if netchange < greatestdecrease[1]:
           greatestdecrease[0] = row[0]
           greatestdecrease[1] = netchange



Financial_analysis= (
                     f"Financial Analysis\n"
                     f"..................\n"
                     f"Total Months: {totalmonths}\n"
                     f"Total: ${totalnet}\n"
                     f"Average Change: ${netmonthlyaverage:.2f}\n"
                     f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n"
                     f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n")


# Print the financial analysis

print(Financial_analysis)

with open(Financialanalysis, "w") as txt_file:
    txt_file.write(Financial_analysis)





*****************************************************8


**PyPoll**

Terminal view:

 

Text file view: 

 

Visual Studio Code:

import os
import csv


Electioncsvpath= os.path.join("Resources", "election_data.csv")
Analysisoutput = os.path.join("Analysis", "election_analysis.txt")

#list of variables
total_votes = 0
Khanvotes= 0
Correyvotes= 0
Livotes= 0
OTooleyvotes= 0

Khan_percentage=0
Correy_percentage=0
Li_percentage=0
OTooley_percentage=0


with open(Electioncsvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    header = next(csvreader)
     

    #calculate the candidate vote
    for row in csvreader:

        # Add to the total vote count
        total_votes = total_votes + 1
        if (row[2]) == "Khan":
            Khanvotes = Khanvotes + 1
        elif (row[2]) == "Correy":
            Correyvotes = Correyvotes + 1
        elif (row[2]) == "Li":
            Livotes = Livotes + 1
        elif (row[2]) == "O'Tooley":
            OTooleyvotes = OTooleyvotes + 1
       
        #Calculate the percentage
        Khan_percentage= round(((Khanvotes/ total_votes)*100),2)
        Correy_percentage= round(((Correyvotes/ total_votes)*100),2)
        Li_percentage= round(((Livotes/ total_votes)*100),2)
        OTooley_percentage=round(((OTooleyvotes/ total_votes)*100),2)

#Find the winner
if Khanvotes> Correyvotes and Khanvotes> Livotes and Khanvotes> OTooleyvotes:
    Winner= "Khan"
elif Correyvotes> Khanvotes and Correyvotes> Livotes and Correyvotes> OTooleyvotes:
    Winner= "Correy"
elif Livotes> Khanvotes and Livotes> Correyvotes and Livotes> OTooleyvotes:
    Winner= "Li"
elif OTooleyvotes> Khanvotes and  OTooleyvotes> Correyvotes and  OTooleyvotes> Livotes:
    Winner= "O'Tooley"


Election_Result= (
                     f"Election Result\n"
                     f"..................\n"
                     f"Total Votes:{total_votes}\n"
                     f"..................\n"
                     f"Khan: {Khan_percentage:.3f}% {Khanvotes}\n"
                     f"Correy: {Correy_percentage:.3f}% {Correyvotes}\n"
                     f"Li: {Li_percentage:.3f}% {Livotes}\n"
                     f"O'Tooley:{OTooley_percentage:.3f}% {OTooleyvotes}\n"
                     f"..................\n"
                     f"Winner: {Winner}\n"
                     f"..................\n")
                                       
print(Election_Result)
# Print the election result

with open(Analysisoutput, "w") as txt_file:
    txt_file.write(Election_Result)
