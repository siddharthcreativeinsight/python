#The pattern useing for loop
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

#useing multiple types of
n=5
for i in range(n):
    p=1
    for j in range(n):
        print(" ",end=" ")
    for k in range(i,n):
        print(p, end=" ")
        p+=1
    print()

#Useing the pattern
m = 5

for f in range(1, m + 1):
    p = 1

    # print spaces
    for s in range(m - f):
        print(" ", end=" ")

    # print numbers
    for j in range(f):
        print(p, end=" ")
        p += 1

    # move to next line
    print()