#list methods
list1=["like","Dislike","share","unshare","unfollow","follow"]
list2=[1,2,3,4,5,6]

#useing a  append
list1.append("Unsubscriptions")
print(list1)

#useing  clear
list2.clear()
print(list2)

#useing a copy
list3=list1.copy()
print(list3)

#useing a length
d=[1,5,6,3,4,44,22,]
print(len(d))

#extend to add tow list in one list
cars=["audio","F1","ford"]
bike=["R1","R6","MT-15","310RR","310R"]
bike.extend(cars)
print(bike)

#useing index
print(bike[0])
print(bike[1])
print(bike[2])
print(bike[-3])


#useing inset
bike.insert(-5,"R4")
print(bike)

#useing pop
cars.pop(2)
print(cars)

#useing remove
bike.remove("R6")
print(bike)

#useing revers
bike.reverse()
print(bike)

#useing sort
list1.sort()
print(list1)
print(len(list1))