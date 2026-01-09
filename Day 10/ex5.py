#Removes the duplicates sets
setname={"bike","cars","plans",}
setname.remove("bike")
print(setname)

#useing union and intersection
newtable={"stud6","bcom","bca","bc","bvoc","stud5"}
newtow={"stud1","stud2","stud3","stud4","stud5","stud6"}
new=newtable | newtow
print(new)

newth=newtable & newtow
print(newth)