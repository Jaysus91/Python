# For loops (Hooray MATLAB again!)
# Add break to stop the loop at a specific point or under certain conditions
for i in range(0,10):
    print(i)
    break

string1="Python"
for character in string1:
    print(character)

# While loops
x=10
while x>0:
    print("{}".format(x))
    x-=1
print("Happy New Year!")

# While loop with a break 
questions=["What is your name?","What is your quest?"]
n=0
while True:
    print("Type q to quit")
    answer = input(questions[n])
    if answer == "q":
        break
    n+=1
    if n>1:
        n=0

# Continue, stops under certain conditions then continues after
for i in range(1,6):
    if i ==3:
        continue
    print(i)
# Nested Loops
for i in range(1,3):
    print(i)
    for letter in ['a','b','c']:
        print(letter)

