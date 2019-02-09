# import modules to read budget data 
import os
import csv
# define file path as variable
budget_data_path = os.path.join("budget_data.csv")
# open and read budget data csv file
with open(budget_data_path, newline="") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter = ",")
#skip Header
    csv_header = next(budget_data_reader)
#set variables to zero
    total_months = 0
    total_change_months = 0
    total_profit_loss = 0
    total_changes = 0
    first_row = True
    previous_row = 0
    monthly_changes = []
    date_list = []
#loop through each row in data
    for row in budget_data_reader:
# count rows in file as total months
        total_months += 1
# sum profit/loss column
        total_profit_loss += int(row[1])
#average change over entire period
#subtract previous row profit/loss from current row profit/loss
        if first_row == False:
            total_change_months += 1
            change = int(row[1]) - int(previous_row)
#append change and date to lists
            monthly_changes.append(int(change)) 
            date_list.append(row[0])
# sum monthly changes
            total_changes += int(change) 
# divide total changes by total months to get average change
            avg_change = round((total_changes/total_change_months),2)                
# max profit
            greatest_increase = max(monthly_changes)
            gi_index = monthly_changes.index(greatest_increase)
            gi_date = date_list[gi_index]
# min profit(loss)
            greatest_decrease = min(monthly_changes)
            gd_index = monthly_changes.index(greatest_decrease)
            gd_date = date_list[gd_index]
#set previous row to current row at the end of each loop
        first_row = False
        previous_row = row[1]
# print analysis results to terminal 
    print("Financial Analysis:")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(total_profit_loss))
    print("Average Change: $" + str(avg_change))
    print("Greatest Increase in Profits: $"+str(greatest_increase)+ " as of " + str(gi_date))
    print("Greatest Decrease in Profits: $"+ str(greatest_decrease)+" as of " + str(gd_date))
    
# create results text file
results_file = "budget_data_results.txt"
# open & write results to text file 
with open(results_file, "w") as txtfile:
#write results to file
    txtfile.write("Financial Analysis: \n")
    txtfile.write("-------------------------------------\n")
    txtfile.write("Total Months: " + str(total_months)+"\n")
    txtfile.write("Total Profit/Loss: $" + str(total_profit_loss)+"\n")
    txtfile.write("Average Change: $" + str(avg_change)+"\n")
    txtfile.write("Greatest Increase in Profits: $"+str(greatest_increase)+ " as of " + str(gi_date)+"\n")
    txtfile.write("Greatest Decrease in Profits: $"+ str(greatest_decrease)+" as of " + str(gd_date)+"\n")