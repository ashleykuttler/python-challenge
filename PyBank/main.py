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
    previous_row = 0 # !!instead of zero how do i define the first month change as null or skip it
    monthly_changes = []
    date_list = []

    for row in budget_data_reader:
# count rows in file as total months
        total_months += 1
# sum profit/loss column
        total_profit_loss += int(row[1])
# average change over entire period
    #subtract previous row profit/loss from current row profit/loss
       # !! if previous_row = row[1]:
        change = int(row[1]) - int(previous_row)
#append change and date to lists
        monthly_changes.append(int(change)) 
        date_list.append(row[0])
    # total changes
        total_changes += int(change) 
    # divide total changes by total months  
        avg_change = round((total_changes/total_months),2)                
# max profit
        greatest_increase = max(monthly_changes)
        gi_index = monthly_changes.index(greatest_increase)
        gi_date = date_list[gi_index]
# min profit(loss)
        greatest_decrease = min(monthly_changes)
        gd_index = monthly_changes.index(greatest_decrease)
        gd_date = date_list[gd_index]
#set previous row to current row at the end of each loop
        previous_row = row[1]
# print analysis results
    print("Financial Analysis:")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(total_profit_loss))
    print("Average Change: $" + str(avg_change))
    print("Greatest Increase in Profits: $"+str(greatest_increase)+ " on " + str(gi_date))
    print("Greatest Decrease in Profits: $"+ str(greatest_decrease)+" on " + str(gd_date))
   
# create path for results csv file
results_path = os.path.join("budget_data_results.csv")
# open & write results to file defined as csv file delimited by ""
with open(results_path, "w", newline ="") as csvfile:
    results_writer = csv.writer(csvfile)
#write results to file
    results_writer.writerow(["Financial Analysis: "])
    results_writer.writerow(["-------------------------------------"])
    results_writer.writerow(["Total Months: " + str(total_months)])
    results_writer.writerow(["Total Profit/Loss: $" + str(total_profit_loss)])
    results_writer.writerow(["Average Change: $" + str(avg_change)])
    results_writer.writerow(["Greatest Increase in Profits: $"+str(greatest_increase)+ " on " + str(gi_date)])
    results_writer.writerow(["Greatest Decrease in Profits: $"+ str(greatest_decrease)+" on " + str(gd_date)])