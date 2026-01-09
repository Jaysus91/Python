# Problem 1
print(min(2,3,4))

# Problem 2
print(min(max(3,4),abs(-5)))
print(abs(min(4, 6, max(2, 8))))

# Problem 3
# Define a function that has one parameter, a number, and returns the number tripled.
def triple_number(x):
    return x*3
print(triple_number(3))

# Problem 4
# define a function that has two parameters, both of which are numbers, 
# and returns the absolute value of the difference of the two.
def abs_diff(x,y):
    return abs(x-y)
print(abs_diff(10,34))

# Problem 5
# define a function that has oneparameter, a distance in 
# kilometers, and returns the distance in miles.
def km_to_miles(kilometers: float):
    miles = kilometers / 1.6
    return miles 
print(km_to_miles(34.5))

# Problem 6
# define a function that has three parameters, grades between 0 and 100 
# inclusive, and returns the average of those grades.
def grades(grade1: int, grade2: int, grade3: int):
    avg = (grade1+grade2+grade3)/3
    return avg
print(grades(100,34,79))

# Problem 7 
# define a function that has four parameters, all of them grades 
# between 0 and 100 inclusive, and returns the average of the best 
# 3 of those grade
def best_grades(grade1, grade2, grade3, grade4):
    grades = [grade1,grade2,grade3,grade4]
    best3 = sorted(grades, reverse=True)[:3]
    average = sum(best3)/len(best3)
    print(average)
    return average

best_grades(10, 100, 80, 90)

# Problem 8
# Complete the examples in the docstring and then write the body 
# of the following function:
def weeks_elapsed(day1, day2):
    """ (int, int) -> int 
    day1 and day2 are days in the same year. 
    Return the number of full weeks that have elapsed between the two days.
    weeks_elapsed(3, 20)
    2
    """
    days_difference = day2-day1
    full_weeks = abs(days_difference // 7)
    print(full_weeks)
    return full_weeks

weeks_elapsed(55, 10)

# Problem 10
def square(num):
    square = num**2
    print(square)
    return square
square(9)
