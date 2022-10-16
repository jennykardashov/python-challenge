from fileinput import close
import os
import csv
from time import clock_getres

#Define the variables
months = []
profit_loss_changes = []

total_months = 0
net_profit_loss = 0
prev_profit_loss = 0
curr_profit_loss = 0
profit_loss_change = 0

# Define path
csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row 
    csv_header = next(csvfile)

    print(f"header: {csv_header}")

    #Read through rows
    for row in csvreader:

        # The total number of months included in the dataset
        total_months += 1
        #print(total_months)

        # The net total amount of "Profit/Losses" over the entire period
        curr_profit_loss = int(row[1])
        net_profit_loss += curr_profit_loss
        # print (curr_profit_loss)

        # Change the index to match the month
        if (total_months == 1):
          prev_profit_loss = curr_profit_loss - prev_profit_loss

          # Add the months 
          months.append(row[0])

          # Change current month loss to prev month loss for next iteration
          prev_profit_loss = curr_profit_loss

        else:
          # Calculate the change in profit loss
          profit_loss_change = curr_profit_loss - prev_profit_loss

          # Add the months
          months.append(row[0])

          # Add the profit loss change to profit loss change
          profit_loss_changes.append(profit_loss_change)

          # Change current month loss to prev month loss for next iteration
          prev_profit_loss = curr_profit_loss

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    total_profit_loss = sum(profit_loss_changes)
    avg_profit_loss = round(total_profit_loss/(total_months -1), 2)
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Define the index of the value for the greatest increase in profits (date and amount) over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)
    greatest_month = months[highest_month_index]
    lowest_month = months[lowest_month_index]

# Print results
output = """ Financial Analysis 
----------------------------
Total Months: %s
Total: $%s
Average Change: $%s
Greatest Increase in Profits: %s ($%s)
Greatest Decrease in Profits: %s ($%s)
""" % (total_months, net_profit_loss, avg_profit_loss, greatest_month, highest_change, lowest_month, lowest_change)
print(output)

# Output
f = open("Analysis/output.txt", "w")
f.write(output)
f.close()