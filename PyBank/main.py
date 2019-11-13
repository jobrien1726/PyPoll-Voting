import os
import csv

budget_data = os.path.join("budget_data.csv")

months = []
profit = []
changeinprofit = []

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        
NumMonths = len(months)
NetProfit = sum(profit)

for i in range(len(profit)-1):
    ChangeInProfit = profit[i+1] - profit[i]
    changeinprofit.append(ChangeInProfit)

AvgChangeInProfit = sum(changeinprofit) / len(changeinprofit)

MaxChangeInProfit = max(changeinprofit)
MinChangeInProfit = min(changeinprofit)
max_change_index = changeinprofit.index(MaxChangeInProfit)
min_change_index = changeinprofit.index(MinChangeInProfit)   

print("Financial Analysis")
print("------------------------------------------------")        
print("Total Number of Months: " + str(NumMonths))
print("Net Total Profit/Losses: " + str(NetProfit))
print("Average Change in Profit: " + str(AvgChangeInProfit))
print("Greatest Increase In Profit: " + months[max_change_index + 1] + " (" + str(MaxChangeInProfit) + ")")
print("Greatest Decrease In Profit: " + months[min_change_index + 1] + " (" + str(MinChangeInProfit) + ")")


txt_file_path = os.path.join("pybank.txt")

with open(txt_file_path, 'w') as pybank:

    pybank.write('Financial Analysis\n')
    pybank.write('------------------------------------------------\n')
    pybank.write('Total Number of Months: ' + str(NumMonths) + '\n')
    pybank.write('Net Total Profit/Losses: ' + str(NetProfit) + '\n')
    pybank.write('Average Change in Profit: ' + str(AvgChangeInProfit) + '\n')
    pybank.write('Greatest Increase In Profit: ' + months[max_change_index + 1] + ' (' + str(MaxChangeInProfit) + ')\n')
    pybank.write('Greatest Decrease In Profit: ' + months[min_change_index + 1] + ' (' + str(MinChangeInProfit) + ')\n')
