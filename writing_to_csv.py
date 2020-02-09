import random
import csv
char="abcdefghijklmnopqrstuvwxyz"
#a="".join((random.choice(char) for i in range(11)))
fname_list=[]
lname_list=[]
for j in range(10000):
    counter1="".join((random.choice(char) for i in range(6)))
    fname_list.append(counter1)

for k in range(10000):
    counter2="".join((random.choice(char) for p in range(4)))
    lname_list.append(counter2)

with open("multi_user.csv",'w', newline="") as fp:
    thewriter=csv.writer(fp)
    thewriter.writerow(["Sl.No","firstname","lastname","Email"])
    for m in range(1,10000):
        thewriter.writerow([m, fname_list[m],lname_list[m], fname_list[m]+"."+lname_list[m]+"@sis.com"])

#data in dictionary form using the DictReader and DictWriter classes










