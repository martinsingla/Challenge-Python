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
    dates = []

    #First loop to find Total and Balance
    for i in csvreader:
        month_counter = month_counter + 1
        balance = balance + int(i[1])

        #Create lists with current and previous valies
        cur_val.append(int(i[1]))
        prev_day.append(prev_val)
        prev_val = int(i[1])
        dates.append(i[0])
    
    #remove 1st value of the list
    cur_val.pop(0)
    prev_day.pop(0)
    dates.pop(0)

    #Calculate difference between initial value previous day value
    dif = []
    for j in range(len(cur_val)):
        dif.append(cur_val[j] - prev_day[j])
    
    #Calculate avg change daily
    averageDailyChange = round(sum(dif) / len(dif), 2)

    #Find max and min values
    maxV = max(dif)
    minV = min(dif)
    maxDate = dates[dif.index(maxV)]
    minDate = dates[dif.index(minV)]

    #Print summary of results
    print("FINANCIAL ANALYSIS")
    print("-----------------------------")
    print(f'Total months: {month_counter}')
    print(f'Total Profit/Losses: ${balance}.-')
    print(f'Average Daily Change: ${averageDailyChange}')
    print(f'Greatest Profit Increase: ${maxV}.- (date: {maxDate})')
    print(f'Greatest Profit Decrease: ${minV}.- (date: {minDate})')

#Export txt file w/ results
textFile = open("Analysis/Results.txt", mode= 'w')
textFile.write("FINANCIAL ANALYSIS\n")
textFile.write("-----------------------------\n")
textFile.write(f'Total months: {month_counter}\n')
textFile.write(f'Total Profit/Losses: ${balance}.-\n')
textFile.write(f'Average Daily Change: ${averageDailyChange}\n')
textFile.write(f'Greatest Profit Increase: ${maxV}.- (date: {maxDate})\n')
textFile.write(f'Greatest Profit Decrease: ${minV}.- (date: {minDate})\n')
textFile.close()
