# Boolean operators
def is_positive(x: float) -> bool:
    print(x>0)
    return x>0

is_positive(2)
is_positive(-1)

def say_the_month():
    month=input('Type the month in format MTH ')
    if len(month) == 3:
        if month == 'Jan':
            print('January')
        else:
            print('Not January')
    else:
        print("Wrong format")
    return 
say_the_month()

def different(a,b):
    if a != b:
        print('True')
    else:
        print('False')
    return 
different(2,2)

area = 1000
pop=int(input('Type the population '))
if pop/area > 100:
    print('Densely populated')
else:
    print('Sparsely populated')



def temp():
    t=float(input('Type the temperature '))
    source=input('Type the source unit: F, C, K - ')
    target=input('Type the target unit: ')
    
    if source == 'F':
        temp_c= (t-32)/1.8
    elif source == 'C':
        temp_c=t
    elif source == 'K':
        temp_c=t-273.15
    
    if target == 'C':
        result=temp_c
    elif target == 'F':
        result=(temp_c*1.8)+32
    elif target == 'K':
        result = temp_c+273.15
    print (f'Result: {round(result,2)}')        
temp()

ph=2
if ph < 7.0:
    print(ph, "is acidic")
if ph < 3.0:
    print(ph, "is very ACIDIC")