# Searching and Sorting
from typing import Any
def linear_search(lst:list, value: Any):
    i = 0
    while i != len(lst) and lst[i] != value:
        i = i+1
    if i == len(lst):
        return -1
    else:
        return 1

lis = [1,2,3,4,5]
result=linear_search(lis, 6)
print(result)
result=linear_search(lis, 4)
print(result)

# Alternate method using for loop (more effective)
# 
# def linear_search(lst: list, value: Any) -> int:
#     for i in range(len(lst)):
#         if lst[i] == value:
#             return i
#     return -1

print(lis.index(5))