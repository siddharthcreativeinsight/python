# calul programmer
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=input("Enter the choice +,-,*,**:")
if c=='+':
    print(f"{a}+{b}={a + b}")
elif c=='-':
    print(f"{a}-{b}={a - b}")
elif c=='*':
    print(f"{a}*{b}={a * b}")
else:
    print(f"choice is {a} and {b}={a**b}")


