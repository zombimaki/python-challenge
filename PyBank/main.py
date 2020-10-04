################################################################################################
# Author: Andrew Perez
# Date: 10/4/2020
# Assignemnt: Homework - Python - PyBank
################################################################################################

# import libraries
import os
import csv

# set the path of the input file
budget_data = os.path.join('.', 'resources', 'budget_data.csv')

# set path of the output file
output_path = os.path.join('.', 'analysis', 'financial_analysis_output.txt')

# Read through the budget data
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # set variables for a month counter, total dollars, and the previous profit loss value
    total_months = 0
    total_dollar = 0
    prev_profit_loss = 0

    # Create ists to store data for the profit/loss difference and the date so we can match these up
    profit_loss_diff = [] 
    profit_loss_date = []

    # ignore the header for our aggregations
    row = next(csvreader,None)

    # loop through the csv and set values to our variables
    for row in csvreader:
        
        if total_months == 0: 
            prev_profit_loss = float(row[1]) #set the prev balance for the first entry
        else:
            monthly_change = float(row[1]) - prev_profit_loss #calculate the difference from the prev record
            profit_loss_diff.append(monthly_change) #append the monthly change to the profit_loss_diff list
            profit_loss_date.append(row[0]) #append the date to the profit_loss_date list
            prev_profit_loss = float(row[1]) #set the prev_profit_loss value to the current profit loss value

        total_months += 1 #add to the total month counter
        total_dollar += int(row[1]) #add to the total dollars
    
  
# calculate the avg, min, and max changes
avg_change = round(sum(profit_loss_diff)/len(profit_loss_diff), 2)
max_change = int(max(profit_loss_diff))
min_change = int(min(profit_loss_diff))
max_change_date = str(profit_loss_date[profit_loss_diff.index(max(profit_loss_diff))])
min_change_date = str(profit_loss_date[profit_loss_diff.index(min(profit_loss_diff))])

# create variable to hold to output strings

output_header = 'Financial Analysis'
output_separator = '----------------------------'
output_months = 'Total Months: ' + str(total_months)
output_ttl_dollars = 'Total: $' + str(total_dollar)
output_avg_change = 'Average Change: $' + str(avg_change)
output_increase = 'Greatest Increase in Profits: ' + str(max_change_date) +' ($'+ str(max_change) + ')'
output_decrease = 'Greatest Decrease in Profits: ' + str(min_change_date) +' ($'+ str(min_change) + ')'

# print output strings to the terminal

print(output_header)
print(output_separator)
print(output_months)
print(output_ttl_dollars)
print(output_avg_change)
print(output_increase)
print(output_decrease)

# write output strings to the output file

output_file =  open(output_path, 'w')
output_file.write(output_header)
output_file.write("\n")
output_file.write(output_separator)
output_file.write("\n")
output_file.write(output_months)
output_file.write("\n")
output_file.write(output_ttl_dollars)
output_file.write("\n")
output_file.write(output_avg_change)
output_file.write("\n")
output_file.write(output_increase)
output_file.write("\n")
output_file.write(output_decrease)
output_file.close()