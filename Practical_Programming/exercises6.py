import math
# Problem 1
print(math.floor(-2.8))
b=abs(round(-4.3))
print(b)

c= math.ceil(math.sin(34.5))
print(c)

# Problem 2
import calendar
d2=calendar.isleap(2028)
print(d2)
f2=calendar.leapdays(1999,2051)
print(f2)
g2=calendar.weekday(2016,7,29)
print(g2)

# Problem 3
import doctest
def average(num1, num2):
    """Returns the average of num1 and num2
    >>> average(10,20)
    15.0
    >>> average(2.5,3.0)
    2.75
    """
    return (num1+num2)/2
print(average(30,40))
doctest.testmod()