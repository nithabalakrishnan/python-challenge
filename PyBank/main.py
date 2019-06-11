import csv
import os 
def readingBudgetData():

    # file paths
    PyBankBudgetcsvPath=os.path.join('Resources','PyBank_Resources_budget_data.csv')
    PyBankBudgetOutputPath=os.path.join('Resources','Results.txt')

    # read csv file
    with open(PyBankBudgetcsvPath, mode='r') as csvfile:
        pyBankBudgetReader = csv.reader(csvfile, delimiter=",")
        next(pyBankBudgetReader) # Skip header
        
        # variable declarations
        totalProfitOrLoss = 0.0
        changeArray = []
        previousValue = -1.0
        changeAverage = 0.0
        maxChange = -9999999.0
        minChange = -9999999.0
        maxProfitDataSet = {}
        minProfitDataSet = {}
        numberOfMonths = 0

        for row in  pyBankBudgetReader:
            currentValue = float(row[1])
            numberOfMonths += 1
            if previousValue != -1:
                change = currentValue - previousValue
                changeAverage += change

                if maxChange == -9999999.0:
                    maxChange = change
                    maxProfitDataSet["period"] = row[0]
                    maxProfitDataSet["value"] = maxChange
                if minChange == -9999999.0:
                    minChange = change
                    minProfitDataSet["period"] = row[0]
                    minProfitDataSet["value"] = minChange

                if change > maxChange:
                    maxChange = change
                    maxProfitDataSet["period"] = row[0]
                    maxProfitDataSet["value"] = maxChange

                if change < minChange:
                    minChange = change
                    minProfitDataSet["period"] = row[0]
                    minProfitDataSet["value"] = minChange
            
            previousValue = currentValue
            changeArray.append(row[1])
            
            totalProfitOrLoss += currentValue

        #Output file under resources
        f = open(PyBankBudgetOutputPath, "w+")
        f.write("Financial Analysis\n")
        f.write("----------------------------\n")
        f.write("Total Months: {0:d}\n".format(numberOfMonths))
        f.write("Total: ${0:.2f}\n".format(totalProfitOrLoss))
        f.write("Average  Change: ${0:.2f}\n".format(changeAverage / (numberOfMonths - 1)))
        f.write("Greatest Increase in Profits: " + str(maxProfitDataSet['period']) + " " + str(maxProfitDataSet['value']) + "\n")
        f.write("Greatest Decrease in Profits: " + str(minProfitDataSet['period']) + " " + str(minProfitDataSet['value']) + "\n")
        f.close()    
        
        #Consloe Prit
        print("Financial Analysis")
        print("----------------------------")
        print("Total Months: {0:d}".format(numberOfMonths))
        print("Total: ${0:.2f}".format(totalProfitOrLoss))
        print("Average  Change: ${0:.2f}".format(changeAverage / (numberOfMonths - 1)))
        print("Greatest Increase in Profits: " + str(maxProfitDataSet['period']) + " " + str(maxProfitDataSet['value']))
        print("Greatest Decrease in Profits: " + str(minProfitDataSet['period']) + " " + str(minProfitDataSet['value']))
readingBudgetData()


