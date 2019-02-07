#import modules to read election data
import os
import csv
# define file path as variable
election_data_path = os.path.join("election_data.csv")
# open read election data csv file
with open(election_data_path, newline = "") as election_data_file:
    election_data_reader = csv.reader(election_data_file, delimiter = ",")
# skip header
    csv_header = next(election_data_reader)
# set variables to zero
    total_votes = 0
    all_candidates = []
    khan_votes= 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    tally_results = {}

#loop through each row in data
    for row in election_data_reader:
 #total number of votes cast   
        total_votes += 1
#Apend names to a complete list of candidates who received votes
        candidate = row[2]
        if candidate not in all_candidates:
            all_candidates.append(candidate)
#The total number of votes each candidate won &
#The percentage of votes each candidate won
        if row[2] == "Khan":
            khan_votes += 1
            khan_percent = round((khan_votes / total_votes)*100,4)
        elif row[2] == "Correy":
            correy_votes += 1
            correy_percent = round((correy_votes / total_votes)*100,4)
        elif row[2] == "Li":
            li_votes += 1
            li_percent = round((li_votes / total_votes)*100,4)
        elif row[2] == "O'Tooley":
            otooley_votes += 1
            otooley_percent = round((otooley_votes / total_votes)*100,4)

#The winner of the election based on popular vote

#print analysis results to terminal
print("Election Results:")
print("------------------------------")
print("Total Votes: "+ str(total_votes))
print("------------------------------")
print("Khan: "+ str(khan_percent) + "% " +str(khan_votes))
print("Correy: "+ str(correy_percent) + "% "+ str(correy_votes))
print("Li: "+ str(li_percent) + "% "+ str(li_votes))
print("O'Tooley: "+ str(otooley_percent) + "% "+ str(otooley_votes))

print("------------------------------")
print("Winner: ")
print("------------------------------")
