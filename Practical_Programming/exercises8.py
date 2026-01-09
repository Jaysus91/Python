# Problem 1
kingdoms = ['Bacteria','Protozoa', 'Chromista', 'Plantae', 'Fungi','Animalia']
    # print(kingdoms[0])
    # print(kingdoms[-1])
    # print(kingdoms[:3])
    # print(kingdoms[2:5])
    # print(kingdoms[4:])
    # print(kingdoms.clear())

# Problem 2
kingdoms = ['Bacteria','Protozoa', 'Chromista', 'Plantae', 'Fungi','Animalia']
    # print(kingdoms[-6])
    # print(kingdoms[5])
    # print(kingdoms[:-3])
    # print(kingdoms[-4:-1])
    # print(kingdoms[-2:])
    # print(kingdoms.clear())

# Problem 3
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
    # appointments.append('16:30')
    # print(appointments)

    # appointments=appointments + ['16:30']
    # print(appointments)

# Problem 4

    # ids = [4353, 2314, 2956, 3382, 9362, 3900]
    # print(ids)
    # ids.remove(3382)
    # print(ids)
    # print(ids.index(9362))
    # ids.insert(4,4499)
    # print(ids)
    # ids = ids + [5566,1830]
    # print(ids)
    # ids.reverse()
    # print(ids)
    # ids.sort()
    # print(ids)

# Problem 5

aem = [4,12,20,38,56,88]
print(aem[5])
print(aem[-1])

print(len(aem))

aem.sort # or this aem = sorted(aem)
print(aem[-1])

# Problem 6
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
print(temps)
cool_temps = temps[:2]
warm_temps = temps[2:]

print(cool_temps)
print(warm_temps)

temps_in_celcius = cool_temps + warm_temps
print (temps_in_celcius)

# Problem 7
def same_first_last(L: list) -> bool:
    """Precondition: len(L) >= 2
    Return True if and only if first item of the list is the same as the last.
    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    """
    return L[0] == L[-1]

# Put a statement like this in function files so it tests in the file
# but won't run the test when imported into another file as a function.
if __name__ != '__main__':  
    import doctest 
    doctest.testmod(verbose=True)

# Problem 8
def is_longer(L1: list, L2: list) -> bool:
    """Return True if and only if the length of L1 is longer than the length of L2.
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    """
    return len(L1) > len(L2)

# Problem 9
values = [0,1,2]
values[1]=values
print(values[1])

# Problem 10
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[0][1:])
print(units[1][:2])

