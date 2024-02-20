import random
import string

# print(string.ascii_letters)  prints upto atoz in both upper and lower case
# print(string.ascii_lowercase)   prints upto atoz in lower case
# print(string.punctuation)  prints all punctuators 

password_ki_length=12
charValues= string.ascii_letters +string.punctuation + string.digits
password=""

for i in range(password_ki_length):
  password+=random.choice(charValues)

print("your random password generated is:  ",password)
