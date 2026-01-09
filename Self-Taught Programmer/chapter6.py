# String Manipulation
#Triple String needs 3 quotation marks
text="""Line One
    Line two
    Line three"""
print (text)
# Iterable, indexable strings
my_string="JADEN"
print(my_string[0])
print(my_string[2])
print(my_string[4])

# Methods: same as functions, but for objects

# Upper command for uppercase switching
string2="Hi I am Jaden and this is a sentence"
print(string2.upper())
# Lower command for lowercase switching
string2="Hi I am Jaden and this is a sentence"
print(string2.lower())

# Capitalize the first word of every sentence with .capitalize()

# Format: insert a string into any occurance of {}
year_born="2000"
print("Jaden was born in {}".format(year_born))

# Not limited to just one
place_born="North Carolina"
lives_now="Stockholm"
print("Jaden was born in {} in the state of {}. He now lives in {}.".format(year_born,place_born,lives_now))

# Split: choose a character in a string and split it into multiple strings accordingly
string3="I am writing this on a plane. My legs are asleep."
print(string3.split("."))

# Join: add new characters between every one in a string
string4="abc"
join_result="+".join(string4)
print(join_result)
# Can join a list of strings into a single string using this.

# Replace: replace every occurance of a character with another
string5="Cat in the Hat"
string5=string5.replace("a","@")
print(string5)

# Escaping: use \ to escape quotes in strings
string6="I once said \"Viva la viva.\""
print(string6)

# New line: \n inside string
print("Line 1 \nLine 2")

# Strings can be multiplied
string7="cat"
print(string7*3)