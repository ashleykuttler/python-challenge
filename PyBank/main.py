# import modules to read budget data 
import os
import csv
budget_data_path = os.path.join("budget_data.csv")

with open(budget_data_path, newline='') as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter = ',')

    csv_header = next(budget_data_reader)
    print(str(csv_header))
# Create variables

# Interate through data and perform aggregations and calculations

# Write final results to text file 