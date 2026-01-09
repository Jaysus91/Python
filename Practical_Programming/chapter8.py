# Storing Data using Lists
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
# >>> whales[0]
# 5
# >>> whales[1]
# 4
# >>> whales[12]
# 1

# >>> whales[-1]
# 3
# >>> whales[-2]
# 1
# >>> whales[-14]
# 5

third = whales[2]
print('Third day:',third)

# Lists can contain strings, integers, and floating point numbers

# Type annotations for lists
from typing import List
def average(L: List[float]):
    avg = sum(L)/len(L)
    print(avg)
    return 
average([5,10,15])

# List operators on page 135, table 10

# Mutable parameters
from typing import List, Any
def remove_last_item(L: List[Any]):
    del L[-1]

list1=['Jaden','Aysa','Nala','Charlie']
remove_last_item(list1)
print(list1)

# List methods on page 142, table 11

# Nested list - example
life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
print(life[0])
print(life[1])

print(life[1][0])
print(life[1][1])

canada=life[0]
print(canada)
print(canada[1])