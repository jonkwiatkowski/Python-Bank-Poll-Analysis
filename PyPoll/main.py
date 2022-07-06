import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

BallotID = []

County = []

Candidate = []

# Read csv and build lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:

        BallotID.append(row[0])

        County.append(row[1])

        Candidate.append(row[2])

# Delete headers
del BallotID[0]
del County[0]
del Candidate[0]

TotalVotes = len(BallotID)




# Print results
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(TotalVotes))
print("--------------------------------")

print("--------------------------------")
print("Winner: ")