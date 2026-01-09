# Working with files
# -------------------------------------
# my_file=open("my_file.txt","w")
# y_file.write("Hello from Python!")
# my_file.close()

# Better format for the same thing

# with open("my_file.txt","r") as my_file:
#    for line in my_file.read():
#        print(line)

import csv

with open ('my_file.csv','w') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=',')
    spamwriter.writerow(['one','two','three'])
    spamwriter.writerow(['four','five','six'])