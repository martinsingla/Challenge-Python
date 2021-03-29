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
    county_list =  []
    county_tot_votes = []

    full_votes_county_list = []
    full_votes_cand_list = []

    for i in csvreader:

        #count total votes
        tot_vote_counter = tot_vote_counter + 1
        
        #identify individual candidates and votes
        if (i[2] not in candidate_list):
            candidate_list.append(i[2])
            candidate_votes.append(0)
        
        if (i[2] in candidate_list):
            candidate_votes[candidate_list.index(i[2])] += 1

        #Identify individual counties and tot votes per county
        if (i[1] not in county_list):
            county_list.append(i[1])
            county_tot_votes.append(0)
        
        if (i[1] in county_list):
            county_tot_votes[county_list.index(i[1])] += 1

        full_votes_county_list.append(i[1])
        full_votes_cand_list.append(i[2])
    
    #quantify % per candidate and count tot. votes
    candidate_per = []
    for j in range(len(candidate_list)):
        candidate_per.append(round(candidate_votes[j] / tot_vote_counter * 100, 3))

    #Identify Winner
    winner = candidate_list[candidate_votes.index(max(candidate_votes))]

    #Make dictionary with counties / candidates / votes per candidate
    county_candidates = {}
    for h in county_list:
        county_candidates[h] = {}
        for l in candidate_list:
            county_candidates[h][l] = 0
    
    for p in range(len(full_votes_cand_list)):
        county_candidates[full_votes_county_list[p]][full_votes_cand_list[p]] += 1

    #Print SUMMARY RESULTS
    print("STATE ELECTION RESULTS")
    print("--------------------------")
    print(f"STATE TOTAL VOTES: {tot_vote_counter}")
    print("--------------------------")
    for j in range(len(candidate_list)):
        print(f'{candidate_list[j]}: {candidate_per[j]}% ({candidate_votes[j]} votes)')
    print("-------------------------- \n")
    print(f'STATE WINNER: {winner} \n')
    print("--------------------------")

#WRITE TEXT FILE WITH FULL RESULTS
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
for k in range(len(county_list)):
    textFile.write(f'COUNTY: {county_list[k]} \n')
    textFile.write(f'Votes: {county_tot_votes[k]} ({round(county_tot_votes[k]/tot_vote_counter * 100, 3)}% of state total) \n\n')
    k_tot = 0
    for f in candidate_list:
            k_tot= k_tot + county_candidates[county_list[k]][f]
    for g in candidate_list:
        textFile.write(f'{g}: {round(county_candidates[county_list[k]][g] / k_tot *100, 2)}% ({county_candidates[county_list[k]][g]} votes)\n')
    textFile.write("\n----------------------------------------------------------\n")
textFile.write("==========================================================\n")

