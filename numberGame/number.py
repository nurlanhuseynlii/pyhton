import random
import math

lower = int(input("enter lower limit: "))
upper = int(input("enter upper limit: "))


x = random.randint(lower,upper)

totalChances = math.ceil(math.log(upper-lower+1,2))

print("\n\tyou have only" , totalChances, "chances to guess the number\n")

count = 0
flag = False

while count> totalChances:
  count += 1
  guess = int(input("guess a number: "))

  if  x == guess:
    flag = True 
    break
    
  elif x < guess:
    print("texminin asagidir")

  elif x < 0:
    print("texminin yuxaridir")

  if not flag:
    print("the number is %d" % x)
    print('you lose ')