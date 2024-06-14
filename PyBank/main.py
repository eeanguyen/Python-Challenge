## Instructions: 
    #our task is to create a Python script that analyzes the records to calculate each of the following values:

    # The total number of months included in the dataset DONE

    # The net total amount of "Profit/Losses" over the entire period DONE

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes DONE

    # The greatest increase in profits (date and amount) over the entire period DONE

    # The greatest decrease in profits (date and amount) over the entire period DONE

# import libraries/modules
import os
import csv

# path to the .csv file
csvPath = os.path.join("Resources", "budget_data.csv")

# Open and read the csvfile
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Skip and Store Header Row for all instances moving forward
    csvHeader = next(csvReader)

    # Set variables
    totalMonths = 0
    netTotal = 0
    revChanges = []
    gInc = [" ", 0]
    gDec = [" ", 0]
    pLoss = 0
    
    
    # Start For Loop
    for row in csvReader:

        # Find Total Months
        totalMonths += 1

        # Find net total amount by converting row 1 into an integer and adding it all together
        netTotal += int(row[1])


        # Find net change in 'Profit/Losses' and calculate the average
        if totalMonths == 1:
            # Reference Column 1 for 'Profit/Loss' and convert from str to int
            pLoss = int(row[1])
        else:
            change = int(row[1]) - pLoss
            # Append the calculated change in the revChanges
            revChanges.append(change)
            pLoss = int(row[1])
            # Average = Sum of list / Length of list
            averageChange = sum(revChanges) / len(revChanges)

             # Find Greatest Inc and Greatest Dec and connect the corresponding date by using the index [1] = 'Profit/Loss' [0] = Date
            if change >gInc[1]:
                gInc = [row[0], change]
            elif change < gDec[1]:
                gDec = [row[0], change]

# Set text path to print Outputs
outputFile = "output.txt"

# Connect Output.txt file
with open (outputFile, 'w') as file:

    #to the follwing print statements, using the file=file method
    print("Financial Analysis", file=file)
    print("------------------", file=file)
    print(f"Total Months: {totalMonths}", file=file)
    print(f"Total: ${netTotal}", file=file)
    print(f"Greatest Increase in Revenue: {gInc[0]} (${gInc[1]})", file=file)
    print(f"Greatest Decrease in Revenue: {gDec[0]} (${gDec[1]})", file=file)

# Get feedback that it has successfully populated in outputFile
print("Financial analysis results have been written to file:", outputFile)