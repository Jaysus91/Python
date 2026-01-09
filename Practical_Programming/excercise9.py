# Problem 1
c_p = ['Emb','Him','Unc','Lon','Dpy','Sma']
for i in range(len(c_p)):
    print(c_p[i])

# Problem 2
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for i in range(len(half_lives)):
    print(half_lives[i],end=' ')
    print()

# Problem 3
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = list(range(len(whales)))
for i in range(len(whales)):
    more_whales[i] = whales[i] + 1
print(more_whales)
print(whales)
    
# Problem 4
alkaline_earth_metals = [[4,12,20,38,56,88],[9.012,24.305,40.078,87.62,137.327,226]]
number_weight = list(range(len(alkaline_earth_metals[0])*2))
print(number_weight)
for i in range(len(alkaline_earth_metals[0])):
    print(alkaline_earth_metals[0][i], alkaline_earth_metals[1][i])

for i in range(len(alkaline_earth_metals[0])):
    number_weight[2*i] = alkaline_earth_metals[0][i]
    number_weight[2*i+1] = alkaline_earth_metals[1][i]
print(number_weight)

# Alternate solution from Gemini
# for x, y in zip(alkaline_earth_metals[0], alkaline_earth_metals[1]):
#     number_weight.append(x)
#     number_weight.append(y)

# Problem 5
def mystery_function(values: list) -> list:
    """ Returns a list or nested list that is reversed

    >>> mystery_function([1,2,3])
    [3,2,1]
    >>> mystery_function([[1,2,3],[4,5,6]])
    [3,2,1],[6,5,4]

    """
    result = [] # Create empty list
    for sublist in values: # checks sublists 
        result.append([sublist[0]]) # creates new sublist containing just the first item of original sublist
        for i in sublist[1:]: # for index i in sublist from 1:end
            result[-1].insert(0, i) # insert the value at the front of the list
    return result

# Problem 6
text = 'QUIT'
text = text.lower()
print(text)

# Problem 7
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for i in country_populations:
    total += i
print('Total pop is',total,'million people')

# Problem 8
rat_1 = [20.5, 21.2, 21.8, 22.5, 23.1, 23.4, 24.0, 24.5, 24.9, 25.4]
rat_2 = [20.0, 22.8, 23.7, 24.5, 25.1, 26.0, 26.8, 27.2, 27.9, 20.5]

# Solution without nested if statements
for w1 in rat_1:
    if rat_1[0] > rat_2[0]:
        print('Rat 1 weighed more than Rat 2 on day 1')
        break
    else:
        print('Rat 2 weighed more than Rat 1 on day 1')
        break
for w2 in rat_2:
    if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
        print('Rat 1 remained heavier')
        break
    else:
        print('Rat 2 became heavier')
        break

# Solution with nested if statements
for w1 in rat_1:
    if rat_1[0] > rat_2[0]:
        print('Rat 1 weighed more than Rat 2 on day 1')
        if rat_1[-1] > rat_2[-1]:
            print('Rat 1 stayed heavier')
            break
        else:
            print('Rat 2 became heavier')

# Problem 9
nums = list(range(33,50))
print(nums)

# Problem 10
print(list(range(10,0,-1)))
# or 
print(list(reversed(range(1,11))))

# Problem 11
pro11 = list(range(2,23))
print(sum(pro11)/len(pro11))

# Problem 12
from typing import List
def remove_neg(num_list: List[float]) -> None:
    for item in range(len(num_list)-1, -1, -1):
        if num_list[item] < 0:
            num_list.pop(item)
    # alternate solution
    # for item in num_list[:]: 
    #   if item < 0:
    #       num_list.remove(item)
    print(num_list)
        
remove_neg([1,2,-1,-3,5,7,-4,6])

# Problem 13
def triangle():
    count = 1
    for i in range(1,8):
        print('T'*count)
        count += 1
triangle()

# Alternate solution
# def triangle():
#     # Outer loop: i will be 1, then 2, then 3... up to 7
#     for i in range(1, 8):
#         # Inner loop: runs 'i' times for the current row
#         for j in range(i):
#             print('T', end='') # end='' prevents a new line after every 'T'
#         print() # This prints a "newline" to move to the next row
        
triangle()
print('-----------')

# Problem 14
def triangle():
    T = ['T']*7
    for i in range(len(T)+1):
        print(' '*(7-i),'T'*i)
triangle()

# Problem 16
rat_1_weight = 250.0
rat_2_weight = 250.0
rat_1_rate = 0.06
rat_2_rate = 0.05
weeks = 0
# a
# while rat_1_weight < 250*1.25:
#     rat_1_weight += rat_1_weight*rat_1_rate
#     weeks += 1
# print('It took',weeks,'weeks for the rat to weigh',rat_1_weight)

while rat_1_weight < 1.1*rat_2_weight:
    rat_1_weight += rat_1_weight*rat_1_rate
    rat_2_weight += rat_2_weight*rat_2_rate
    weeks += 1
print('It took',weeks,'weeks for the rat 1 to weigh 10% more than Rat 2')
