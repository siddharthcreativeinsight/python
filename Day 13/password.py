#ceating a password
import random
import string

#the length
length=8

#use the password
password = string.ascii_letters+string.digits+string.punctuation

# creating password
password = "".join(random.sample(password,length))

#The password print
print("Your password is:",password)