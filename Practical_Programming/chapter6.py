import math
from temperature import *

convert_to_celcius(212)
above_freezing(0)

print('name is', __name__)

if __name__ == '__main__':
    f=float(input('Enter the temp in deg F: '))
    c = convert_to_celcius(f)
    if above_freezing(c):
        print('It is above freezing.')
    else:
        print('It is below freezing.')

import doctest
doctest.testmod