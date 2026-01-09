# Integer Division gives just the integer of division
# 53 // 24 produces 2

# Modulo gives just the remainder of division
# 53 % 24 produces 5

# See Table 2 (Page 15) for Operator Precedence, Table 1 for all other operators (Page 13)
# Online visualizer on page 17

# See Table 3 (Page 22) augmented operators

# Practice Problems
a = 9-3
b = 8*2.5
c = 9/2
d = 9/-2
e = 9//-2
f = 9 % 2
g = 9.0 % 2
h = 9 % 2.0
i = 9 % -2
j = -9 % 2
k = 9 / -2.0
l = 4 + 3 * 5
m = (4+3)*5

print(a,b,c,d,e,f,g,h,i,j,k,l,m)

# Problem 2
x = -17
x = +x
print(x)

# Problem 3
temp = 24
temp_f = (1.8 * temp) - 32
print(temp_f)

# Problem 5
x5 = 10.5
y5 = 4
x5=x5+y5
print(x5)
print(y5)

# Problem 6
x6 = 3
x6 += x6-x6
print(x6)
# x6 will evaluate out to 3 because Python evaluates the right side first so (3-3) \
# then the result is added to the original x6
