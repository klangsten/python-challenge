# Import the modules 
import csv
import os
#Files to load and output 
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidates = {}

#Fowllow the "chocolate cake recipe" for reading a CSV
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    #Read the header
    header = next(reader)

    # For each row:
    for row in reader:

        total_votes = total_votes + 1

        name = row[2]

        if name not in candidates:
            #add the candidate to the vote_count
            candidates[name] = 1
        else:
            #Increment the vote count for the candidate
            candidates[name] = candidates[name] + 1

print(total_votes) 

for candidate_name, vote_count in candidates.items():
    print(f"{candidate_name}: {vote_count}") 