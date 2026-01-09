def calculator_jaden():
    while True:
        print("Press q to quit.")
        c=input("Type 1 for +, 2 for -, 3 for *, 4 for /\n")
        if c=="q":
            break
        a=input('Number 1\n')
        b=input('Number 2\n')
        a=float(a)
        b=float(b)
        c=float(c)
        if c==1:
            print("Answer is:")
            print(a+b)
        if c==2:
            print("Answer is:")
            print(a-b)
        if c==3:
            print("Answer is:")
            print(a*b)
        if c==4:
            try:
                print("Answer:")
                print(a/b)
            except ZeroDivisionError:
                print("Number 2 cannot be zero. Try again\n")
