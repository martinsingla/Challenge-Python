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

    prev_val = "NaN"
    cur_val = []
    prev_day = []

    dif = []

    for i in csvreader:
        month_counter = month_counter + 1
        balance = balance + int(i[1])

        cur_val.append(int(i[1]))
        prev_day.append(prev_val)
        prev_val = int(i[1])
    
    cur_val.pop(0)
    prev_day.pop(0)

    for j in range(len(cur_val)):
        dif.append(cur_val[j] - prev_day[j])

    

    print("FINANCIAL ANALYSIS")
    print("-----------------------------")
    print(f'Total months in period: {month_counter}')
    print(f'Profit/Losses for perior: ${balance}.-')

    print(cur_val)
    print(prev_day)
    print(dif)







