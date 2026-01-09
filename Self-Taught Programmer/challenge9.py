# Program that collects data and saves it to a file
import csv

print("Enter data with commas separating each entry.\n")
a=input("Enter your name, birth year, and the city you live in.\n")
    
list = (a)

with open ('challenge9.csv','w') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=',')
    spamwriter.writerow([a])
