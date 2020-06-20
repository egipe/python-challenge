import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Declare all variables
vote_count = 0

# Create blank list and dictonary
candidates = []
candidates_dict = {}
candidate_votes = []
candidate_percentage = []

# Define the function 
def election_results(election_csv):
    # Declare Global Values
    global vote_count

    # The total number of votes cast
    vote_count +=1

    # Append Candidate list with candidate name
    if row[2] not in candidates:
        candidates.append(row[2])
        candidates_dict[row[2]] = 1

    # number of votes + 1
    else: 
        candidates_dict[row[2]] = candidates_dict[row[2]] + 1
    
    # Count the number of candidate votes
    # calculate the percentage for given candidate vote/ total vote * 100

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through the data
    for row in csvreader:
        # call function
        election_results(row)

print("Election Results")
print("-----------------------")
print(f"Total Votes: {str(vote_count)}")
print("-----------------------")

# Create file
data_output = os.path.join("analysis", "election_analysis.txt")
with open(data_output, 'w') as datafile:
    datafile.write("Election Results \n")
    datafile.write("----------------------- \n")
    datafile.write(f"Total Votes: {str(vote_count)} \n")
    datafile.write("----------------------- \n")

# Loop through the established dictionary to set vote, percentage and winner

winner = ""
max_votes = 0

for candidate in candidates_dict: 
    candidate_vote = candidates_dict.get(candidate)
    candidate_percentage = candidate_vote / vote_count * 100
    # Print each time it loops through the dictionary
    print(f"{str(candidate)}: {int(candidate_percentage)}% ({str(candidate_vote)})")
    # Add these to the open file
    with open(data_output, 'a+') as datafile:
        datafile.write(f"{str(candidate)}: {int(candidate_percentage)}% ({str(candidate_vote)}) \n")

    if candidate_vote > max_votes:
        winner = candidate 
        max_votes = candidate_vote

print("-----------------------")
print(f"Winner: {str(winner)}")

with open(data_output, 'a+') as datafile:
    datafile.write("----------------------- \n")
    datafile.write(f"Winner: {str(winner)}")


