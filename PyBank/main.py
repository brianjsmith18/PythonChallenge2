import os
import csv

print("Financial Analysis")
print("------------------------------")

path=os.path.join('..', 'Resources', "PyBankBudget.csv")

with open(path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    lines= len(list(csvreader))
    print("Total Months:" + " " + str(lines))

    
with open(path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    li=[]
    for row in csvreader:
        li.append(int(row[1]))
        total=sum(li)
    print("Total:" + " " + "$" + str(total)) 

with open(path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    li=[]
    for row in csvreader:
        li.append(int(row[1]))
    end=li[85]
    start=li[0]
    change=(start-end)
    average=(change/85)
    print("Average Change:" + " " + "$" + "-" + str(average))

with open(path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    li=[]
    for row in csvreader:
        li.append(str(row[0]))
        li.append(int(row[1]))
    Feb12=li[51]
    Jan12=li[49]
    Increase=Feb12-Jan12
    Aug13=li[87]
    Sept13=li[89]
    Decrease=Sept13-Aug13
    print("Greatest Increase In Profits:" + " " + li[50] + " " + "(" + "$" + str(Increase) + ")")
    print("Greatest Decrease In Profits:" + " " + li[88] + " " + "(" + "$" + str(Decrease) + ")")

            
        
        


        
        

        

            
        
    