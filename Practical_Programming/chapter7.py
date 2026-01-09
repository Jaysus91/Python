# Page 119 & 120 has a table of all str methods
my_pi = 3.14159
print('Pi rounded to {0} decimal places is {1:.2f}.'.format(2,my_pi))
print('Pi rounded to {} decimal places is {:.3f}.'.format(3,my_pi))

print('hello'.upper())
print('Happy Birthday!'.lower())
print('WeEeEeEeEe'.swapcase())
print('ABC123'.isupper())
print('aeiouAEIOU'.count('a'))
print('hello'.endswith('o'))
print('Hello {}'.format('Python'))

# Problem 2
t = 'tomato'
x2 = t.count('o')
print(x2)

# Probelm 3
x3 = t.find('o')
print(x3)

# Problem 4
x4=t.find('o',t.find('o')+1)
print(x4)

# Problem 5
a = 'avocado'
print(a.find('o',a.find('o')+1))

# Problem 6
r = 'runner'.replace('n','b')
print(r)

# Problem 7
s='  yes  '
print(s)
print(s.strip())

# Problem 8
fruit = 'pineapple'
print(fruit.find('p',fruit.count('p')))
print(fruit.count(fruit.upper().swapcase()))
print(fruit.replace(fruit.swapcase(),fruit.lower()))

# Problem 9
season='summer'
print('I love {}'.format(season))

# Problem 10
side1=3
side2=4
side3=5
print('The sides have the length of {}, {}, and {}'.format(side1, side2, side3))

# Problem 11
boole='boolean'
print(boole.upper())
ch='CO2 H2O'
print(ch.find('2'))
print(ch.find('2',ch.find('2')+1))
if boole[0].islower():
    print('True')
else:
    print('False')
mon='MoNDaY'
mon=mon.lower().capitalize()
print(mon)
mon2='  MOnday'
mon2=mon2.lstrip()
print(mon2)

# Problem 12
def total_occurences(s1: str, s2: str, ch: str):
    """Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
>>> total_occurrences('color', 'yellow', 'l')
    3
>>> total_occurrences('red', 'blue', 'l')
>>> total_occurrences('green', 'purple', 'b')
    """
    ch=ch.lower()
    s1 = s1.lower()
    s2 = s2.lower()
    total = s1.count(ch) + s2.count(ch)
    print(total)
    return

total_occurences('color', 'yellow', 'l')
