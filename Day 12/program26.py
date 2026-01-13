#error handling
try:
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    result=num1/num2
    print("result", result)
except ZeroDivisionError:
    print("Error,You cannot divide by zero")
except NameError:
    print("Error, Please enter a valid number:")
else:
    print("Success!")
finally:
    print("program are successfully finished")