# Import Dependancies
import os, csv
from pathlib import Path

# Request file name for input and output
input_file = Path("/Users/algend/Data-Homework/Data-Homework/PyBank/budget_data.csv")

# Declare and track variables
total_months = 0
total_revenue = 0.0
last_revenue = 0.0
avg_revenue = 0.0
average_change = []
increase_profits =[]
decrease_profits = []
month_switch = []
revenue_change = []

# Read files
with open(input_file, mode = "r", newline="", encoding="utf-8") as budgetdata:

# Store in contents in variable csvreader
    csvreader = csv.reader(budgetdata,delimiter=",")

# Skip the header labels to initiate iteration loop
    header = next(csvreader)

    for row in csvreader:

# Iteration to gather the output
        if(total_months==0):
                last_revenue = float(row[1])
        else:
                revenue_change.append((float(row[1]) - last_revenue))
                last_revenue = float(row[1])
                month_switch.append (row[0])
        total_months = total_months + 1
        total_revenue = total_revenue + float (row[1])                      

# Average revenue change calculation
avg_revenue= sum(revenue_change) / len(revenue_change) 

# Profit increase calculation 
increase_profits = list(zip (month_switch, revenue_change))
max_val=max(increase_profits, key = lambda x:x[1])
min_val=min(increase_profits,key = lambda x:x[1])

# Print Data Output
print("Financial Analysis")
print("______________________________")
print(f"Total Months: {total_months}")
print(f"Total Revenue: $ {int(total_revenue)}")
print(f"Average Change: ${round(avg_revenue,2)}")
print(f"Greatest Increase in Profits: {max_val[0]} (${int(max_val[1])})")
print(f"Greatest Decrease in Profits: {min_val[0]} (${int(min_val[1])})")

# Write to data file
with open("/Users/algend/Data-Homework/Data-Homework/PyBank/Analysis.txt", mode = "w") as output_file:
        output_file.write("Financial Analysis\r\n")
        output_file.write("______________________________\r\n")
        output_file.write(f"Total Months: {total_months}\r\n")
        output_file.write(f"Total Revenue: ${int(total_revenue)}\r\n")
        output_file.write(f"Average Change: ${round(avg_revenue,2)}\r\n")
        output_file.write(f"Greatest Increase in Profits: {max_val[0]} (${int(max_val[1])})\r\n")
        output_file.write(f"Greatest Decrease in Profits: {min_val[0]} (${int(min_val[1])})\r\n")