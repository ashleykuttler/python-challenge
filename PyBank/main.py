# import modules to read budget data 
import os
import csv
# define file path as variable
budget_data_path = os.path.join("budget_data.csv")
# open and read budget data csv file
with open(budget_data_path, newline="") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter = ",")
#Skip Header
    csv_header = next(budget_data_reader)
#set variables to zero
    total_months = 0
    total_profit_loss = 0
    total_changes = 0
    previous_row = 0 # !!instead of zero how do i define the first row change as null or none
    monthly_changes = []

    for row in budget_data_reader:
# count rows in file as total months
        total_months += 1
# sum profit/loss column
        total_profit_loss += int(row[1])
# average change over entire period
    #subtract previous row profit/loss from current row profit/loss
        change = int(row[1]) - int(previous_row)
    # append change to list of changes
        monthly_changes.append(int(change)) # !!add date to monthly changes
    # total changes
        total_changes += int(change)
    # divide total changes by total months  
        avg_change = round((total_changes/total_months),2)                
# max profit
        greatest_increase = max(monthly_changes) # !!split elements to call max and corresponding date?
# min profit(loss)
        greatest_decrease = min(monthly_changes)
#set previous row to current row at the end of each loop
        previous_row = row[1]
# print analysis results
    print("Financial Analysis:")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(total_profit_loss))
    print("Average Change: $" + str(avg_change))
    print("Greatest Increase in Profits: $"+str(greatest_increase)+ " on ")
    print("Greatest Decrease in Profits: $"+ str(greatest_decrease)+" on ")
   

   
# create path for results file
results_path = os.path.join("budget_data_results.csv")
# Write final results to text file 
with open(results_path, "w", newline ="") as csvfile:
    results_writer = csv.writer(csvfile)
    #!! figure out syntax for writing results to new file
    #results_writer.writerow(["Financial Analysis: "], [f"Total Months:  {total_months}"])