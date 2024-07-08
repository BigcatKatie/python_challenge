# Import the csv modules
import csv
from pathlib import Path

# Define the file path
file_path = Path('Resources') / 'election_data.csv'

# Create variables
# Use to count the total number of votes
total_votes=0

# Use to store the number votes each candidate received
candidate_votes = {}

# Read the csv files
with file_path.open('r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        total_votes += 1
        candidate = row [2]
        
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
candidate_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentage[candidate]
    print(f"{candidate}:{percentage:.3f}% ({votes})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Export the results to a text file
with open('analysis/election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentage[candidate]
        file.write(f"{candidate}: {percentage: 0.3f}% ({votes})\n")
    file.write("--------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------\n")
    