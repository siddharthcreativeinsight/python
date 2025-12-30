#for loop
Bike=["yamaha" , "TVS" , "Honda","Ninja" ,"Royal Enfield"]
for x in Bike:
    print(x)

#looping
for x in Bike:
    print(x)
    if x == "Ninja":
      break

#continue looping statement
for x in Bike:
    if x == "TVS":
        continue
    print(x)

#checking a number  loop
for a in range(10):
    print(a)

#check a tow number rage
for b in range(5 , 15):
    print(b)

#check a program for three number in for loop
for c in range(1 , 10 , 2):
    print(c)

#useing Nested loop
College=["Christ College", "RKU College" , "Grace College" , "Marwadi College"]
for x in College:
    for y in range(1,5):
        print(y,x)

# while loop
i=1
while i<10:
    print(i)
    i=i+1
else:
    print("i is loger then 10")


#while loop
X=10
y=20
while y<=X:
    print(y, end=" ")
    i=i+1
else:
      print("exit")



