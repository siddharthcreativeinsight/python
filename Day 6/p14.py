#check the prima number
n=int(input("Enter the Number:"))
def sum(n):
    flag=0
    for i in range(2, n):
        if n == 1 or n == 2:
            return False
        if n % i == 0:
            flag=1
            break
    if flag==1:
        print("This is not prima number.",n)
    else:
        print("This is prima number.",n)
sum(n)

