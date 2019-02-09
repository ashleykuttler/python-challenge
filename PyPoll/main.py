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
    cd0_votes= 0
    cd1_votes = 0
    cd2_votes = 0
    cd3_votes = 0
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
#append tally results to dictionary
        if row[2] == all_candidates[0]:
            cd0_votes += 1
            cd0_percent = round((cd0_votes / total_votes)*100,4)
            tally_results.update({all_candidates[0]:cd0_votes})
        elif row[2] == all_candidates[1]:
            cd1_votes += 1
            cd1_percent = round((cd1_votes / total_votes)*100,4)
            tally_results.update({all_candidates[1]:cd1_votes})
        elif row[2] == all_candidates[2]:
            cd2_votes += 1
            cd2_percent = round((cd2_votes / total_votes)*100,4)
            tally_results.update({all_candidates[2]:cd2_votes})
        elif row[2] == all_candidates[3]:
            cd3_votes += 1
            cd3_percent = round((cd3_votes / total_votes)*100,4)
            tally_results.update({all_candidates[3]:cd3_votes})

# find max value in dictionary retrieve KEY to find winner based on popular vote
    winner = max(tally_results, key=tally_results.get)
#print analysis results to terminal
print("Election Results:")
print("------------------------------")
print("Total Votes: "+ str(total_votes))
print("------------------------------")
print(all_candidates[0]+": " + str(cd0_percent) + "% " +str(cd0_votes))
print(all_candidates[1]+": " + str(cd1_percent) + "% "+ str(cd1_votes))
print(all_candidates[2]+": " + str(cd2_percent) + "% "+ str(cd2_votes))
print(all_candidates[3]+": " + str(cd3_percent) + "% "+ str(cd3_votes))
print("------------------------------")
print("Winner: "+ str(winner))
print("------------------------------")

#create results file text
results_file = "election_data_results.txt"
#open and write results to text file
with open(results_file, "w") as txtfile:
#write results to file
    txtfile.write("Election Results:\n")
    txtfile.write("------------------------------\n")
    txtfile.write("Total Votes: "+ str(total_votes)+"\n")
    txtfile.write("------------------------------\n")
    txtfile.write(all_candidates[0]+": " + str(cd0_percent) + "% " +str(cd0_votes)+"\n")
    txtfile.write(all_candidates[1]+": " + str(cd1_percent) + "% "+ str(cd1_votes)+"\n")
    txtfile.write(all_candidates[2]+": " + str(cd2_percent) + "% "+ str(cd2_votes)+"\n")
    txtfile.write(all_candidates[3]+": " + str(cd3_percent) + "% "+ str(cd3_votes)+"\n")
    txtfile.write("------------------------------\n")
    txtfile.write("Winner: "+ str(winner)+"\n")
    txtfile.write("------------------------------")

