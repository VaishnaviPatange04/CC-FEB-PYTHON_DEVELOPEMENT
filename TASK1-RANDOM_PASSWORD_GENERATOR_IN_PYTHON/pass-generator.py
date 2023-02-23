import random

lowercase = "abcdefghijklmnopkrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
characters = "!@#$%*_"
password = ""

for i in range(8, 16):
    password = password + random.choice(lowercase + uppercase + digits + characters)

print("Password: "+ password)