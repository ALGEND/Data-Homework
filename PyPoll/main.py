# Import Dependancies
import os, csv
from pathlib import Path

# Request file name for input and output
input_file = Path("/Users/algend/Data-Homework/Data-Homework/PyPoll/election_data.csv")

# Declare and track variables
total_votes = 0
winner = 0
percentage = []
vote = []
candidate = []
candidate_list = []
final_winner = []

# Read files
with open(input_file, mode = "r", newline="", encoding="utf-8") as electionsdata:

# Store in contents in variable csvreader
    csvreader = csv.reader(electionsdata,delimiter=",")

# Skip the header labels to initiate iteration loop
    header = next(csvreader)

# Iteration to gather the output
    for row in csvreader:
        total_votes = total_votes + 1
        if(row[2] not in candidate):
            candidate.append(row[2])
            vote.append(1)
        else:
            candidate_list = candidate.index(row[2])
            vote[candidate_list] = vote[candidate_list] + 1
    
#Percentage calculation loop
for i in range(len(candidate)):
    percentage.append(round((vote[i]/total_votes)*100,4))

final_list = list(zip(candidate, percentage, vote))

final_winner = sorted(final_list, key = lambda x:x[1], reverse=True)

    
#Print output
print(f" Election Results")
print(f" ----------------------------------------------")
print(f" Total Votes: {total_votes}")
print(f" ----------------------------------------------")
for i in range(len(final_winner)):
    print(f" {final_winner[i][0]}: {final_winner[i][1]}% ({final_winner[i][2]})")
print(f" Winner: {final_winner[0][0]}")

# Write to data file
with open("/Users/algend/Data-Homework/Data-Homework/PyPoll/Analysis.txt", mode = "w") as output_file:
    output_file.write(f" Election Results\r\n")
    output_file.write(f" ----------------------------------------------\r\n")
    output_file.write(f" Total Votes: {total_votes}\r\n")
    output_file.write(f" ----------------------------------------------\r\n")
    for i in range(len(final_winner)):
        output_file.write(f"{final_winner[i][0]}: {final_winner[i][1]}% ({final_winner[i][2]})\r\n")
    output_file.write(f" Winner: {final_winner[0][0]}\r\n")
    