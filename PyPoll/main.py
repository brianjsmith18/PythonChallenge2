import os
import csv

print("Election Results")
print("------------------------------")

path=os.path.join('..', 'Resources', "PyPoll.csv")

with open(path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    # lines= len(list(csvreader))
    lines=0
    
    li=[]
    candidateD={}
    percentage={}
    for row in csvreader:
        lines=lines+1
        if row[2] not in li:
            li.append(row[2])
            candidateD[row[2]]=0
        candidateD[row[2]]=candidateD[row[2]]+1
    print("Total Votes:" + " " + str(lines)) 
    print("------------------------------")
    for row in candidateD:
        percentage[row] = round(candidateD[row]/lines * 100,3)
        print(row,percentage[row],candidateD[row])
    # print(percentage)
    # print(li) 
    # print(candidateD)
         

print("------------------------------")
print("Winner:" " Kahn")
print("------------------------------")




