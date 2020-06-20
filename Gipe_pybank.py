import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Declare all variables
month_count = 0
total = 0
previous_profit = 0 
previous_change = 0
current_change = 0
greatest_increase_month = ""
greatest_increase_change = 0
greatest_decrease_month = ""
greatest_decrease_change = 0
change_count = 0

# Define the function 
def budget_analysis(budget_row):
    # declare variables as global 
    global month_count
    global total
    global previous_profit
    global previous_change
    global current_change
    global greatest_increase_change
    global greatest_decrease_change
    global greatest_increase_month
    global greatest_decrease_month
    global change_count

    # increase month counter by 1 on each loop
    month_count += 1
    # increase the total by the volume in the profits losses column
    total = total + int(budget_row[1]) 
    
    # Check first to see if it is not the first row
    if month_count > 1:
        current_change = int(budget_row[1]) - previous_profit
        if current_change > greatest_increase_change:
            greatest_increase_change = current_change
            greatest_increase_month = str(budget_row[0])
        if current_change < greatest_decrease_change:
            greatest_decrease_change = current_change
            greatest_decrease_month = str(budget_row[0])
    else:
        previous_profit = budget_row[1]

    # set previous profit amount
    change_count = change_count + current_change
    previous_profit = int(budget_row[1])
    previous_change = current_change

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through the data
    for row in csvreader:
        # call function
        budget_analysis(row)

# Calculate the average
average_change = change_count / month_count

# Print budget stats
print(f"Total Months: {str(month_count)}")
print(f"Total: ${str(total)}")
print(f"Average Change: {str(average_change)}")
print(f"Greatest Increase in Profits: {str(greatest_increase_month)} (${str(greatest_increase_change)})")
print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} (${str(greatest_decrease_change)})")

# create CSV
data_output = os.path.join("analysis", "budget_analysis.txt")

with open(data_output, 'w') as datafile:
    datafile.write(f"Total Months: {str(month_count)} + \n")
    datafile.write(f"Total: ${str(total)}+ \n")
    datafile.write(f"Average Change: {str(average_change)} + \n")
    datafile.write(f"Greatest Increase in Profits: {str(greatest_increase_month)} (${str(greatest_increase_change)}) + \n")
    datafile.write(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} (${str(greatest_decrease_change)})")
