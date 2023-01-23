# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))
# Method 2: Improved Reading using CSV module
date_list = []
profit_loss_list = []
with open(csvpath) as csvfile:
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
       # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        date_list.append(row[0])
        profit_loss_list.append(int(row[1]))
with open("Analysis/results.txt","w") as result_file:
    # The total number of months included in the dataset
    print("total month "+str(len(date_list)))
    result_file.write("total month "+str(len(date_list)))
    result_file.write("\n")
    # The net total amount of "Profit/Losses" over the entire period
    print("total $"+str(sum(profit_loss_list)))
    result_file.write("total $"+str(sum(profit_loss_list)))
    result_file.write("\n")
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    change_list = []
    for previous, next in zip(profit_loss_list,profit_loss_list[1:]):
        change_list.append(next-previous)
    print("Average Change $"+ str(round(sum(change_list)/len(change_list),2)))
    result_file.write("Average Change $"+ str(round(sum(change_list)/len(change_list),2)))
    result_file.write("\n")
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period
    min_val = change_list[0]
    max_val = change_list[0]
    min_idx = 0
    max_idx = 0
    for i,change in enumerate(change_list[1:],1):
        if change >max_val:
            max_val = change
            max_idx = i
        if change <min_val:
            min_val = change
            min_idx = i
    print("Greatest Increase in Profits " + date_list[max_idx] +" $"+ str(max_val))
    result_file.write("Greatest Increase in Profits " + date_list[max_idx] +" $"+ str(max_val))
    result_file.write("\n")
    print("Greatest Decrease in Profits " + date_list[min_idx] +" $"+ str(min_val))
    result_file.write("Greatest Decrease in Profits " + date_list[min_idx] +" $"+ str(min_val))
    result_file.write("\n")
