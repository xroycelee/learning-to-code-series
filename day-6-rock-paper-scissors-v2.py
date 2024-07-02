
from random import randint

print("Welcome to the game of rock, paper, scissors")
player = input("Player please pick your move: ").lower()
#robot move
random_number = randint(1,3)
if random_number == 1:
    robot = "rock"
elif random_number == 2:
    robot = "paper"
else:
    robot = "scissors"
print(f"Robot chose {robot}")

if player == robot:
    print("It's a draw!")
elif player == "rock":
    if robot == "scissors":
        print("Player wins!")
    elif robot == "paper":
        print("Robot wins!")
elif player == "paper":
    if robot == "rock":
        print("Player wins!")
    elif robot == "scissors":
        print("Robot wins!")
elif player == "scissors":
    if robot == "paper":
        print("Player wins!")
    elif robot == "rock":
        print("Robot wins!")
else:
    print("Opps, something went wrong! Only pick 'rock', 'paper', 'scissors'.")