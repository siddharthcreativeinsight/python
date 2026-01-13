#handle invalid input by using the try and except block
try:
    user1 = int(input("Enter a number: "))
    user2 = int(input("Enter another number: "))
    result = user1-user2
    print("result"==result)
except ValueError:
    print("Invalid input please enter a number!")
except ZeroDivisionError:
    print("Invalid input please enter a number!")
except NameError:
    print("Invalid input please enter a number!")
else:
    print("Calculation complete.")
finally:
    print("program finished.")
