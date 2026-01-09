# Page 69 has a table of escape seequences for strings

# Print keyword arguments
#print('a','b','c',sep=', ')
#print('a','b','c')
#print('a','b','c',sep=', ', end='')

# Practice Problems

print('"he said, \'Absolutely not\'" recalled Mel.')

print('A\nB\nC')

x = 3
y = 12.5

print('The rabbit is',x)
print('The rabbit is',x,'years old')
print(y,'is average')
print(x,'*',y)

num = float(input('Type a number '))
print(num)

# Problem 8
def repeat(s: str, n: int) -> str:
    """Return s repeated n times; if n is negative, return the empty string"""
    print(s*n)
    return s*n
repeat('Jaden',-3)

# Problem 9
def total_length(s1: str, s2: str) -> int:
    x=len(s1)
    y=len(s2)
    print(x+y)
    return x+y
total_length('jaden','hamid')
