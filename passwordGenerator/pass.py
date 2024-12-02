import random

print("welcome password generator")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+|\:;"

number = int(input("ne qeder parola ehtiyyaciniz var?: "))

length = int(input("parolunun nece reqemli olmagini isteyirsen?: "))

print('they are your password')


for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)
        