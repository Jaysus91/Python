def convert_to_celcius(fahrenheit: float):
    return (fahrenheit-32)* (5/9)

def above_freezing(temp_c):
    return temp_c > 0

if __name__ == '__main__':
    f=float(input('Enter the temp in deg F: '))
    c = convert_to_celcius(f)
    if above_freezing(c):
        print('It is above freezing.')
    else:
        print('It is below freezing.')

