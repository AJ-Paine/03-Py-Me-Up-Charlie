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
        #Find number of votes for Khan
        if voter[2] == 'Khan':
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
        #Find candidate list
        if voter[2] in Candidate_List:
            continue
        else:
             Candidate_List.append(voter[2])
    
    
    #Calcuate percentage of votes and format to 3 decimal points
    Khan_perc = format(Khan_Votes/Total_Votes*100, ".3f")
    Correy_perc = format(Correy_Votes/Total_Votes*100, ".3f")
    Li_perc = format(Li_Votes/Total_Votes*100, ".3f")
    OTooley_perc = format(OTooley_Votes/Total_Votes*100, ".3f")

    if Khan_perc > Correy_perc and Khan_perc > Li_perc and Khan_perc > OTooley_perc:
        winner = "Khan"
    elif Correy_perc > Li_perc and Correy_perc > OTooley_perc:
        winner = "Correy"
    elif Li_perc > OTooley_perc:
        winner = "Li"
    else:
        winner = "O'Tooley"

    #Create Dictionary
    Election_Summary = dict()
    Election_Summary["Candidate"] = Candidate_List
    Election_Summary["Percentage of Vote"] = [Khan_perc, Correy_perc, Li_perc, OTooley_perc]
    Election_Summary["Number of Votes"] = [Khan_Votes, Correy_Votes, Li_Votes, OTooley_Votes]

    #print(Election_Summary)
    #Print Results
    #print(Candidate_List)
    print('Election Results')
    print('---------------------------')
    print(f'Total Votes: {Total_Votes}')
    print('---------------------------')

    #Print via Dictionary
    print(f'{Election_Summary["Candidate"][0]}: {Election_Summary["Percentage of Vote"][0]}% ({Election_Summary["Number of Votes"][0]})')
    print(f'{Election_Summary["Candidate"][1]}: {Election_Summary["Percentage of Vote"][1]}% ({Election_Summary["Number of Votes"][1]})')   
    print(f'{Election_Summary["Candidate"][2]}: {Election_Summary["Percentage of Vote"][2]}% ({Election_Summary["Number of Votes"][2]})')
    print(f'{Election_Summary["Candidate"][3]}: {Election_Summary["Percentage of Vote"][3]}% ({Election_Summary["Number of Votes"][3]})') 
    print('---------------------------')
    print(f'Winner: {winner}')
    print('---------------------------')


    #write output file
    output_path = os.path.join('Analysis', 'PyPoll_Output_AJP.txt')
    with open(output_path, 'w', newline='') as output:
        csvwriter = csv.writer(output, delimiter=',')
        csvwriter.writerow(['Election Results'])
        csvwriter.writerow(['---------------------------'])
        csvwriter.writerow([f'Total Votes: {Total_Votes}'])
        csvwriter.writerow(['---------------------------'])
        csvwriter.writerow([f'{Election_Summary["Candidate"][0]}: {Election_Summary["Percentage of Vote"][0]}% ({Election_Summary["Number of Votes"][0]})'])
        csvwriter.writerow([f'{Election_Summary["Candidate"][1]}: {Election_Summary["Percentage of Vote"][1]}% ({Election_Summary["Number of Votes"][1]})'])
        csvwriter.writerow([f'{Election_Summary["Candidate"][2]}: {Election_Summary["Percentage of Vote"][2]}% ({Election_Summary["Number of Votes"][2]})'])
        csvwriter.writerow([f'{Election_Summary["Candidate"][3]}: {Election_Summary["Percentage of Vote"][3]}% ({Election_Summary["Number of Votes"][3]})'])
        csvwriter.writerow(['---------------------------'])
        csvwriter.writerow([f'Winner: {winner}'])
        csvwriter.writerow(['---------------------------'])
        

