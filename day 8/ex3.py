#Tuple Tuple
aTuple=("apple","banana","cherry",1,25,36,15)
print(aTuple)
print(aTuple[1])
print(len(aTuple))
print(type(aTuple))
print(aTuple[-1])
print(aTuple[2:5])


#update the elements
bTuple=list(aTuple)
bTuple[2]="Black cherry"
aTuple = tuple(bTuple)
print(aTuple)

#add item
cTuple=list(aTuple)
cTuple.append('Cherry')
print(cTuple)

DTuple=("water",)
aTuple += DTuple
print(aTuple)

#add loop
cTuple=("R6","Gtr911","F2")
for x in cTuple:
    print(x)

#while loop useing
dTuple=(1,2,3,4)
i=0
while i < len(dTuple):
    print(dTuple[i])
    i=i+1

#remove the elements
s=list(cTuple)
s.remove("R6")
cTuple=tuple(s)
print(cTuple)


