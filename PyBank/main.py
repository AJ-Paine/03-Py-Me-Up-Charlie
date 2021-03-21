# Import Modules
import os
import csv

# Read in CSV File

csvpath = os.path.join('Resources','03-Python_HW_Instructions_PyBank_Resources_budget_data.csv')
#print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Print Headers
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Define Variables
    Total_Months = 0
    Total = 0
    Previouse_Month = str()
    Previous_Month_Profit = 867884
    Previous_Month_Profit_Change = 0
    Current_Month = str()
    Current_Month_Profit = 0
    Current_Month_Profit_Change = 0
    Running_Profit_Change = 0
    Max_Profit_Change = 0
    Max_Profit_Change_Month = str()
    Min_Profit_Change = 0
    Max_Profit_Change_Month = str()

    for row in csvreader:
        #Find Total Months
        Total_Months += 1
        #Find Total Profits/Losses
        Total += int(row[1])
        #Find Average Change
        Current_Month_Profit = int(row[1])
        Current_Month = str(row[0])
        Current_Month_Profit_Change = Current_Month_Profit - Previous_Month_Profit
        if Current_Month_Profit_Change > Max_Profit_Change:
            Max_Profit_Change = Current_Month_Profit_Change
            Max_Profit_Change_Month = Current_Month
        if Current_Month_Profit_Change < Min_Profit_Change:
            Min_Profit_Change = Current_Month_Profit_Change
            Min_Profit_Change_Month = Current_Month
        Running_Profit_Change += Current_Month_Profit_Change
        Previous_Month_Profit = int(row[1])
        Previous_Month = str(row[0])
#Calculate Average Chanage
    Average_Change = round(Running_Profit_Change / (Total_Months-1), 2)
# #Print OutPut Analysis
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${Average_Change}")
    print(f"Greatest Increase in Profits: {Max_Profit_Change_Month} (${Max_Profit_Change})")
    print(f"Greatest Decrease in Profits: {Min_Profit_Change_Month} (${Min_Profit_Change})")



