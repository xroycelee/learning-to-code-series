# Exercise: unlucky number + even + odd number
#loop through 1 - 20
# 4 and 13 are unlucky numbers
# even number print "x is even"
# odd number print "x is odd"

# V1
for n in range(1,21):
    if n == 4 or n == 13:
        print(f"{n} is unlucky")
    elif n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# V2: more concise code
for n in range(1,21):
    if n == 4 or n == 13:
        state = "unlucky"
    elif n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{n} is {state}")



# Exercise: for loop vs while loop
# for loop version:
print("This is a 'for' loop")
for num in range(1,11):
    print(num)

# while loop version:
print("This is a 'while' loop")
num = 1
while num < 11:
    print(num)
    num += 1









# Exercise: while loop - who is the best soccer player in the world?
question = input("Who is the best soccer player in the world? ")
while question != "Messi":
    print("wrong!")
    question = input("Who is the best soccer player in the world? ")
print("Correct")








# Exercise: Guessing game
from random import randint
# the random number
num = 0
# number of guesses
i = 0

while num != 10:
    i += 1
    num = randint(1,10)
    print(f"The number is {num}")
print(f"It took {i} tries to get to the number 10")









# Exercise: breaking a loop
while True:
    command = input("Type 'exit' to exit: ")
    if command == 'exit':
        break
print("you have exited")











# Exercise: reminder to stop procrastinating
num = int(input("How many times would you like to be reminded to do your homework? "))
for n in range(num):
    print("Do your homework!")
    if n >= 3:
        print("You need to stop procrastinating")
        break