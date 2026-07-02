try:
    a=int(input("enter first no:"))
    b=int(input("enter second no:"))
    print(a+b)
    print(a/b)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
print("gm") 