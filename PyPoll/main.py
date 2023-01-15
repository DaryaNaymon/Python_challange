# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
#The total number of votes cast
votes_dict = {}
with open(csvpath) as csvfile:
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
       # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        if row[2] not in votes_dict.keys():
            votes_dict[row[2]]= 0
        votes_dict[row[2]]+=1
# The total number of votes cast
total_votes = sum(votes_dict.values()) 
print("Total Votes: " + str(total_votes))
# A complete list of candidates who received votes
for candidate,votes in votes_dict.items():
    print (candidate +" " + str(round((votes/total_votes)*100,2)) +"% (" + str(votes) +")")
winner=list(votes_dict.keys())[0]
max_votes = votes_dict[winner]
for candidate,votes in votes_dict.items():
    if votes >max_votes:
        max_votes = votes
        winner = candidate
    
print("Winner " + winner)