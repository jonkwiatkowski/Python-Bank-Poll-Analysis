import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

Date = []
ProfitLoss = []
Change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:

        Date.append(row[0])

        ProfitLoss.append(row[1])

    # Make sure that the headers aren't included in Date or ProfitLoss lists
    del Date[0]
    del ProfitLoss[0]

    # Cast list as integers
    ProfitLoss = [int(i) for i in ProfitLoss]

    # Build list containing changes in profit/loss
    x = 0
    while x < (len(ProfitLoss)-1):

        Change.append(ProfitLoss[x+1]-ProfitLoss[x])
        x = x + 1

    NumberDates = len(Date)

    Total = sum(int(x) for x in ProfitLoss)

    TotalChange = sum(int(x) for x in Change)

    Average = round(TotalChange/len(Change),2)

    GreatestIncrease = max(Change)

    GreatestDecrease = min(Change)

    GreatestIncreaseDate = Date[Change.index(GreatestIncrease)+1]
    GreatestDecreaseDate = Date[Change.index(GreatestDecrease)+1]

    # Print results

    print("Financial Analysis")

    print("------------------------------------------------")

    print("Total Months: " + str(NumberDates))

    print("Total: $" + str(Total))

    print("Average Change: $" + str(Average))

    print("Greatest Increase in Profits: " + GreatestIncreaseDate + " ($" + str(GreatestIncrease) + ")")

    print("Greatest Decrease in Profits: " + GreatestDecreaseDate + " ($" + str(GreatestDecrease) + ")")