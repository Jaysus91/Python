# Al g rythym's
# Top-down Design
# Write out what needs to be done in plain english, and slowly begin
# to build the code from there on. Much more time efficient.

# Timing code to gauge speed and memory usage
import time
t1 = time.perf_counter()
    # Code to time goes here
t2 = time.perf_counter()
print('The code took {:.2f}ms'.format((t2 - t1) * 1000.))

# Problem 1

# Read the string
# replace the letter with its compliment
# continue down the list
# print result

def compliment(dna: str) -> str:
    pairs = {'A': 'T','T':'A','G':'C','C':'G'}
    comp = ""
    for letter in dna:
        comp += pairs[letter]
    print(comp)
    return
l = 'AATTGCCGT'
compliment(l)

# Problem 2

numbers = [3, 8, 1, 9, 2, 10, 7]
# Start by assuming the first number (index 0) is the smallest
smallest = numbers[0]
position = 0
# Loop through the list starting from the second element
for i in range(1, len(numbers)):
    # Check if the current number is smaller than our record-holder
    if numbers[i] < smallest:
        smallest = numbers[i]  # Update the smallest value
        position = i           # Update the position where we found it

print(smallest, position)

def min_index(n: list) -> tuple:
    smallest = n[0]
    pos = 0
    for i in range(1,len(n)):
        if n[i] < smallest:
            smallest = n[i]
            pos = i
    tup = (smallest,pos)
    return tup

result = min_index(numbers)
print(result)

def min_max_index(num: list, get_min: bool):
    result = num[0]
    position = 0
    for i in range(1,len(num)):
        if get_min == True:
            if num[i] < result:
                result = num[i]
                position = i
        else:
            if num[i] > result:
                result = num[i]
                position = i
    result_tuple = (result,position)
    return result_tuple
result = min_max_index(numbers,False)
print(result)

# Problem 4
