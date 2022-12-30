import random
import string

print('hello, Welcome to Password generator!')

size = int(input('Enter the length of password: '))                      

lett=string.ascii_letters
num = string.digits
spec='!@#$%^&*_-+'

all = lett + spec + num 
for _ in range(3):
    temp = random.sample(all,size)
    password = "".join(temp)
    print(password)
