#Import Modules
import os
import csv

#Read in CSV File
csvpath = os.path.join('Resources', '03-Python_HW_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    pypoll_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(pypoll_data)

    
    Total_Votes = 0
    Candidate_List = []
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    OTooley_Votes = 0

    for voter in pypoll_data:
        #Find total votes
        Total_Votes += 1
        #Find candidate list
        if voter[2] in Candidate_List:
            continue
        else:
            Candidate_List.append(voter[2])
        #Find number of votes for Khan
        if voter[2] == 'Kahn':
            Khan_Votes += 1
        #Find number of votes for Correy
        if voter[2] == 'Correy':
            Correy_Votes += 1
        #Find number of votes for Li
        if voter[2] == 'Li':
            Li_Votes += 1
        #Find number of votes for Correy
        if voter[2] == "O'Tooley":
            OTooley_Votes += 1
    
    
    #Calcuate percentage of votes
    kahn_perc = Khan_Votes/Total_Votes
    Correy_perc = Correy_Votes/Total_Votes
    Li_perc = Li_Votes/Total_Votes
    OTooley_perc = OTooley_Votes/Total_Votes
    
    #Print Results
    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {Total_Votes}')
    print('---------------------')
    print(f'Khan: {Khan_Votes}')
    print(Correy_Votes)
    print(Li_Votes)
    print(OTooley_Votes)
        
# #Create Candidate List
# Candidate_List = []
# for voter in pypoll_data:
#     #Candidate = str(row[2])
#     if row[2] in Candidate_List:
#         continue
#     else:
#         Candidate_List.append(row[2])
#     print(Candidate_List)
#     print(voter)


        

