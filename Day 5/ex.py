
def table(user):
    for x in range(1, 11):
        print(f"{user} * {x} = {user * x}")

for i in range(1, 101):
    print(f"\nTable of {i}")
    table(i)