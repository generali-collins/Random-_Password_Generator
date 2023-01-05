# Collins Wanga


#Random Password Generator
#Import the relevant modules
import random
import string
print ('Hello, Welcome to Random Password Generator')
#Password length
length = int(input('\nEnter the length of the password: '))
#Definitions
upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
#Combine data
all = upper + lower + numbers + symbols
#import random
temp = random.sample(all,length)
password = "".join(temp)
print(password)
