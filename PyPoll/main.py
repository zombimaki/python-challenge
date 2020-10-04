################################################################################################
# Author: Andrew Perez
# Date: 10/4/2020
# Assignemnt: Homework - Python - PyPoll
################################################################################################

# import libraries
import os
import csv

# decalre variables
total_votes = 0 
candidate_votes = []
candidates = []
candidates_pcnt = []
winning_votes = 0
winning_idex = None

# Set the path of the input file
election_data  = os.path.join('.', 'resources', 'election_data.csv')

# set the path of the output file
output_path = os.path.join('.', 'analysis', 'election_summary_output.txt')

#Read through the election data
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # ignore the header for our aggregations
    row = next(csvreader,None)

    #loop through the csv and set values to our variables
    for row in csvreader:

        total_votes += 1 #add to the total month counter
        candidate = row[2] #name of the candidate in the file

        if candidate in candidates:  
            c_idx = candidates.index(candidate)
            candidate_votes[c_idx] += 1 
        else:
            candidates.append(candidate)
            candidate_votes.append(1) 
        

# find the percentage for each candidate and the winner

for i in range(len(candidate_votes)):

    vote_pcnt = round(candidate_votes[i] / total_votes * 100, 3) #divide candidate votes by total votes
    candidates_pcnt.append(vote_pcnt)

    if candidate_votes[i] > winning_votes:
        winning_votes = candidate_votes[i]
        winning_index = i

  
#determine the winning cndidate
winning_candidate = candidates[winning_index]

# create variables to hold to output strings
output_header = 'Election Results'
output_separator = '----------------------------'
output_votes = 'Total Votes: ' + str(total_votes)
output_winner = 'Winner: '+ str(winning_candidate)


# print output strings to the terminal
print(output_header)
print(output_separator)
print(output_votes) 
print(output_separator)

for i in range(len(candidates)):
    print(f'{candidates[i]}: {candidates_pcnt[i]}00% ({candidate_votes[i]})')

print(output_separator)
print(f'Winner: {winning_candidate}')
print(output_separator)

# write output strings to the output file
output_file =  open(output_path, 'w')
output_file.write(output_header)
output_file.write("\n")
output_file.write(output_separator)
output_file.write("\n")
output_file.write(output_votes)
output_file.write("\n")
output_file.write(output_separator)
output_file.write("\n")

for i in range(len(candidates)):
    print(f'{candidates[i]}: {candidates_pcnt[i]}00% ({candidate_votes[i]})', file=output_file)

output_file.write(output_separator)
output_file.write("\n")
output_file.write(output_winner)
output_file.write("\n")
output_file.write(output_separator)
output_file.write("\n")
output_file.close()