a = float(input("enter first number: "))
b = input("choose sign:+,-,/,*,^,  . ")
c = float (input("enter second number: "))

if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    if c!=0:
        print(a/c)
elif b=='^':
    print(a**c)
else:
    print("error! ")

