# Processing list items using a for loop.
velocities = [0,9.81,19.62,29.43]
for velocity in velocities:
    print('Metric:',velocity, 'm/sec;', 
          'Impertial',velocity*3.28,'ft/sec')

# Can be done for strings as well.  
country = 'United States of America'
for ch in country:
    if ch.isupper():
        print(ch)

# Generating Ranges of Numbers
print(range(10))
for num in range(10):
    print(num)

# creates a numbered list from the range, not including stop value
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(5,10)) # [5, 6, 7, 8, 9]

# Can change the step size
list(range(2000, 2020, 4)) #[2000, 2004, 2008, 2012, 2016]
# or reversed for descending sequence
list(range(2020, 2000, -4)) # [2016, 2012, 2008, 2004, 2000]

total = 0
for i in range(1,101):
    total += i
print(total)

values = [4, 10, 3, 8, -6]
for i in range(len(values)):
    print(i, values[i])

# How to change items in a list
values = [4, 10, 3, 8, -6]
print(values)
for i in range(len(values)):
    values[i] *= 2
print(values)

# Processing Parallel Lists using indices
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]
for i in range(len(metals)):
    print(metals[i], weights[i])

# Nesting Loops in Loops
outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)

def print_table(n: int):
    numbers = list(range(1,n+1))
    for i in numbers:
        print('\t'+ str(i), end='')
    print()

    for i in numbers:
        print(i, end='')

        for j in numbers:
            print('\t'+ str(i*j), end='')
        print()
#print_table(5)

# While loops
rabbits = 3
while rabbits > 0:
    print(rabbits)
    rabbits -= 1

time = 0
pop = 1000
gr = 0.21
while pop < 2000:
    pop = pop + pop*gr
    print(round(pop))
    time += 1
print ('It took', time, 'minutes for the pop to double.')
print('The final pop was', round(pop), 'bacteria.')

# Infinite Loops - press ctrl-c or cmd-c in console to kill 
# when an infinite loop is running

text = ''
while text != 'quit':
    text = input('Enter a chemical formula (or \'quit\' to exit):')
    if text.lower() == 'quit':
        print('exiting program')
        break
    elif text == 'H2O':
        print('Water')
    else:
        print('Unknown')


