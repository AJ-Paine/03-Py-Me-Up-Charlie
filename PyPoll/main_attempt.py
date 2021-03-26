#Import Modules
import os
import csv

pypoll_data
#Read in CSV File
csvpath = os.path.join('Resources', '03-Python_HW_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    pypoll_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(pypoll_data)

    #Find Total Votes
    Total_Votes = 0
    for row in pypoll_data:
        Total_Votes += 1
        print(row)
    print(Total_Votes)
        
#Create Candidate List
Candidate_List = []
for voter in pypoll_data:
    #Candidate = str(row[2])
    if row[2] in Candidate_List:
        continue
    else:
        Candidate_List.append(row[2])
    print(Candidate_List)
    print(voter)


        

