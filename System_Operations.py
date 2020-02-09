import os
a=os.getlogin()
b=os.getcwd()
#os.mkdir("New Folder") # Makes directoty in the current working directory.
#os.mkdir("New Folder/sub folder1")
file_path="C:/Users/Admin/Desktop/House.txt"
#print("The current working directory is {0}".format(b))
c=os.path.isfile(file_path)
line="Had one Loss of pay, HRA rent receipts for tax exemption, LTA balance, Leave encashment, queries on other process"
w=len(line.split())
print(w)


