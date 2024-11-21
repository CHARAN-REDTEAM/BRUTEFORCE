import random
number = int(input("Input a number that is password:"))
guess = 0
while(guess !=number):
    guess= random.randint(0,9999)
    print(guess)
    print("your password is"+str(number))