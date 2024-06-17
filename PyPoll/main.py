# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# The total number of votes cast DONE

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# import libraries/modules
import os
import csv

# path to the .csv file
csvPath = os.path.join("Resources", "election_data.csv")

#open and read thecsvfile
with open(csvPath) as csvFile:
    csvReader = csv.reader (csvFile, delimiter=',')

    # Set Variables
    totalVotes = 0
    candidates = []
    candidateVotes = {}
    maxVotes = 0
    winner = ""
    votePercentages = {}

    #Skip and Store Header Row for all instances moving forward
    csvHeader = next(csvReader)

    # Start For Loop
    for row in csvReader:

    #Calculate the total votes casted
        totalVotes += 1
        candidateName = row[2]

        # Add caandidats to list if not already added
        if candidateName not in candidates:
            candidates.append(candidateName)
            candidateVotes[candidateName] = 0

        #Count votes for each candidate
        candidateVotes[candidateName] += 1

    # Determin the winner according to the max amount of votes
    for candidate in candidateVotes:
        votes = candidateVotes[candidate]
        if votes > maxVotes:
            maxVotes=votes
            winner = candidate

    # Calculate each candidates percentages of votes
    for candidate in candidateVotes:
        votes= candidateVotes[candidate]
        percentage = (votes/totalVotes) * 100
        votePercentages[candidate] = percentage

# Set text path to print Outputs
outputFile = "output.txt"

# Connect Output.txt file
with open (outputFile, 'w') as file:
    # to the following statements, using the file = file method
    print("Election Results", file=file)
    print("-------------------------", file=file)
    print(f"Total Votes: {totalVotes}", file=file)
    print("-------------------------", file = file)
    for candidate in candidates:
        print(f"{candidate}: {votePercentages[candidate]:.3f}% ({candidateVotes[candidate]})", file=file)
    print("-------------------------", file=file)
    print(f"Winner: {winner}", file = file)
    print("-------------------------", file = file)

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {votePercentages[candidate]:.3f}% ({candidateVotes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
# Get feedback that it has successfully populated in outputFile
print("Poll results have been written to file:", outputFile)
