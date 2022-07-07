import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

BallotID = []

County = []

Candidate = []

# Read csv and build lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csvheader = next(csvfile)

    for row in csvreader:

        BallotID.append(row[0])

        County.append(row[1])

        Candidate.append(row[2])


TotalVotes = len(BallotID)

#Create empty dictionary
CandidateDict = {}

for i in Candidate:
    # Increment each element that already appears in the dictionary
    if i in CandidateDict:
        CandidateDict[i] += 1
    else:
        CandidateDict[i] = 1 

# Eliminate duplicates
CandidateDict = { candidate:number for candidate, number in CandidateDict.items() if number > 1}

print(CandidateDict)


# Print results
print("Election Results")

print("------------------------------------------")

print("Total Votes: " + str(TotalVotes))

print("------------------------------------------")

for candidate in CandidateDict:
    PercentVotes = round((CandidateDict[candidate]/TotalVotes)*100,3)
    print(f"{candidate} {PercentVotes}% ({CandidateDict[candidate]})")
 
print("-------------------------------------------")
Winner = max(CandidateDict, key=CandidateDict.get)

print(f"Winner: {Winner}")

print("-------------------------------------------")