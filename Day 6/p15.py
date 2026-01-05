#Check factorial number
N=float(input("Check the factorial number:"))
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print("Factorial is",factorial(N))