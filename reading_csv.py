# ####################################################################################################
# Reading a CSV file and printing the output.
# import csv
# with open("family_age.csv",'r') as fp:
#     r=csv.reader(fp)
#     data=list(r)
#     #print(data[1][1])
#     for line in data:
#         for word in line:
#             print(word,"\t",end="")
#         print()

####################################################################################################
import csv
with open("family_age.csv",'r') as fr:
    r=csv.reader(fr)
    data=list(r)

for line in data:
    for word in line:
        print(word,"\t",end="")
        print()

with open("family_age.csv","w") as fw:
    towriter=csv.writer(fw)
    towriter.writerow(data)


