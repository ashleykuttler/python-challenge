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
    for row in budget_data_reader:
# count rows in file as total months
        total_months += 1
# sum profit/loss column
        total_profit_loss += int(row[1])
# average profit/loss column
# loop through data and find max profit
# loop through data and fin min profit(loss)
# print analysis results
    print("Financial Analysis:")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(total_profit_loss))

   

# Write final results to text file 