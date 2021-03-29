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
    candidate_votes = []

    for i in csvreader:

        #count total votes
        tot_vote_counter = tot_vote_counter + 1
        
        #identify individual candidates and votes
        if (i[2] not in candidate_list):
            candidate_list.append(i[2])
            candidate_votes.append(0)
        
        if (i[2] in candidate_list):
            candidate_votes[candidate_list.index(i[2])] += 1

    #quantify % per candidate and count tot. votes
    candidate_per = []
    for j in range(len(candidate_list)):
        candidate_per.append(round(candidate_votes[j] / tot_vote_counter * 100, 3))

    #Identify Winner
    winner = candidate_list[candidate_votes.index(max(candidate_votes))]

    #Loop process for each county

    print("STATE ELECTION RESULTS")
    print("--------------------------")
    print(f"STATE TOTAL VOTES: {tot_vote_counter}")
    print("--------------------------")
    for j in range(len(candidate_list)):
        print(f'{candidate_list[j]}: {candidate_per[j]}% ({candidate_votes[j]} votes)')
    print("-------------------------- \n")
    print(f'STATE WINNER: {winner} \n')
    print("--------------------------")
    print("RESULTS BY COUNTY \n")
    print("--------------------------")

    #print stats per county


#Write results in text file
textFile = open("Analysis/Results.txt", mode= 'w')
textFile.write("==========================================================\n")
textFile.write("                  STATE ELECTION RESULTS\n\n")
textFile.write(f"State Total Votes: {tot_vote_counter}\n")
textFile.write("----------------------------------------------------------\n")
for j in range(len(candidate_list)):
    textFile.write(f'{candidate_list[j]}: {candidate_per[j]}% ({candidate_votes[j]} votes)\n')
textFile.write("---------------------------------------------------------- \n")
textFile.write(f'State Winner: {winner} \n\n\n')
textFile.write("==========================================================\n")
textFile.write("                     RESULTS BY COUNTY \n")
textFile.write("----------------------------------------------------------\n")
textFile.write("                       under dev.\n")
textFile.close()
    


