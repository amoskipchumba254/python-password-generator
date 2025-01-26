import string
import random

def Generate_password(num):
    password = ''
    
    for n in range(num):
        x = random.randint(0, 94)
        password += string.printable[x]
        return password
    
print(Generate_password(16))