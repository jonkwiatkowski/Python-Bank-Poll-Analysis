import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

BallotID = []

County = []

Candidate = []

# Read csv and build lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Store the header
    csvheader = next(csvfile)

    for row in csvreader:

        BallotID.append(row[0])

        County.append(row[1])

        Candidate.append(row[2])

# Finds total number of votes
TotalVotes = len(BallotID)

#Create empty dictionary
CandidateDict = {}

# Build dictionary by ncrementing each element that already appears
for candidate in Candidate:

    if candidate in CandidateDict:
        CandidateDict[candidate] += 1
    else:
        CandidateDict[candidate] = 1 

# Eliminate duplicates keeping only unique candidates as keys and their frequency as values
CandidateDict = {candidate:number for candidate, number in CandidateDict.items() if number > 1}

# Print results
print("Election Results")

print("------------------------------------------")

print("Total Votes: " + str(TotalVotes))

print("------------------------------------------")

for candidate in CandidateDict:
    PercentVotes = round((CandidateDict[candidate] / TotalVotes) * 100,3)
    print(f"{candidate}: {PercentVotes}% ({CandidateDict[candidate]})")
 
print("-------------------------------------------")
Winner = max(CandidateDict, key=CandidateDict.get)

print(f"Winner: {Winner}")

print("-------------------------------------------")