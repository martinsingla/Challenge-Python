#PyPoll Data Analytics Challenge
#Load dependencies
import os
import csv

#Read data
csv_path = os.path.join("Resources/PyPoll_data.csv")
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header= next(csvreader)

    tot_vote_counter = 0
    candidate_list = []

    for i in csvreader:

        #count total votes
        tot_vote_counter = tot_vote_counter + 1
        
        #identify individual candidates
        if (i[2] not in candidate_list):
            candidate_list.append(i[2])


    #quantify % per candidate and count tot. votes

    #Identify Winner



    #Loop process for each county

    print("ELECTION RESULTS")
    print("--------------------------")
    print(f"TOTAL VOTES: {tot_vote_counter} \n")
    print("--------------------------")
    for j in range(len(candidate_list)):
        print(f'{candidate_list[j]}: ')