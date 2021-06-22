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