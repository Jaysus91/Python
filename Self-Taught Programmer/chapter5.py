my_dict={"apple":"red","banana":"yellow"}
print(my_dict)

my_dict["programming"]="tough"

print(my_dict)
print(my_dict["apple"])

a=input("Search the dictionary")
a=str(a)
if a in my_dict:
    print("True")
else:
    print("False")
