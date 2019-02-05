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
    total_ballets = 0
    all_candidates = []
#loop through each row in data
    for row in election_data_reader:
 #total number of votes cast   
        total_ballets += 1
#A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in all_candidates:
            all_candidates.append(candidate)
        

        
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote














#print analysis results to terminal
print("Election Results:")
print("------------------------------")
print("Total Votes: "+ str(total_ballets))
print("------------------------------")

print("------------------------------")
print("Winner: ")
print("------------------------------")
