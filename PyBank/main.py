# Python Challenge 1: PyBAnk
# Basic summary analysis of profit/losses from a company

#Opening file
import os
import csv

csvpath = os.path.join('Resources', 'PyBank_data.csv') # file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #file opener

    csv_header = next(csvreader) #Identify header 
    print(f'CSV Header: {csv_header}')

    month_counter = 0
    balance = 0
    prev_month_val=0
    
    monthly_dif = []

    for i in csvreader:
        month_counter = month_counter + 1
        balance = balance + int(i[1])

        monthly_dif.append(prev_month_val + int(i[1]))
        prev_month_val = int(i[1])
    
    avg_monthly_dig = sum(monthly_dif) / month_counter

    print("Financial Analysis")
    print("-----------------------------")
    print(f'Total months in period: {month_counter}')
    print(f'Profit/Losses for perior: ${balance}.-')
    print(f'Average change: ${avg_monthly_dig}')





