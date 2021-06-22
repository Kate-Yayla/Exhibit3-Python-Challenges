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