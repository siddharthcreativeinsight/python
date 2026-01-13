#Error to user not a give any output
try:
    print(user)
except NameError:
    print("Error the user not give a Number!")
finally:
    print("user are not give a numbers !")