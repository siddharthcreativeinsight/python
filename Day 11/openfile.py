#useing the open and close sta
f = open("demotext.py","r")
print(f.read())
f.close()

with open("demotext.py","a") as f:
    f.write("New line add for new captions")

#to open with new lines
with open ("demotext.py") as f:
    print(f.read())
