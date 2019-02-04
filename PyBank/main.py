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
# count rows in file as total months
    budgetdata = list(budget_data_reader)
    total_months = len(budgetdata)
# sum profit/loss column
# average profit/loss column
# loop through data and find max profit
# loop through data and fin min profit(loss)
# print analysis results
    print("Financial Analysis:")
    print("----------------------------")
    print("Total Months: " + str(total_months))

   

# Write final results to text file 