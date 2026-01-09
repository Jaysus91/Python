# Challenge: create an infinite loop where I guess numbers, have q to quit
import random
i=random.randint(0,100)
while input ("Continue y or n?\n")!="n":
    k=input("Guess the number.\n") 
    k=int(k)
    if i==k:
        print("Correct!\n")
    else:
        print("Try again!\n")
        
        
