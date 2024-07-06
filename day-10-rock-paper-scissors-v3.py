

from random import randint

player_score = 0 #player score
robot_score = 0 #robot score
round_num = 0 #number of rounds 

print("Welcome to the game of Rock Paper Scissors")
rounds = int(input("How many rounds would you like to play? "))
print(f"The one with a higher score after {rounds} rounds will be the winner!")

while round_num < rounds:
    print(f"Player score: {player_score}, Robot score: {robot_score}")
    player = input("Player please pick your move: ").lower()
    if player == "quit" or player == "q":
        print("Player ended the game early.")
        break

    random_num = randint(1,3)
    if random_num == 1:
        robot = "rock"
    elif random_num == 2:
        robot = "paper"
    else:
        robot = "scissors"

    print(f"Robot picked {robot}")

    state = "invalid"

    if player == robot:
        state = "draw"
    elif player == "rock":
        if robot == "scissors":
            state = "player wins"
        elif robot == "paper":
            state = "robot wins"
    elif player == "paper":
        if robot == "rock":
            state = "player wins"
        elif robot == "scissors":
            state = "robot wins"
    elif player == "scissors":
        if robot == "paper":
            state = "player wins"
        elif robot == "rock":
            state = "robot wins"
    else:
        print("Opps, please pick 'rock', 'paper', or 'scissors'.")
    
    round_num += 1
    
    if state == "player wins":
        print("Player wins!")
        player_score += 1
    elif state == "robot wins":
        print("Robot wins!")
        robot_score += 1
    elif state == "draw":
        print("It's a draw")
    else:
        print("That's an invalid choice, you wasted 1 round!")

print(f"The final score is... Player score: {player_score}, Robot score: {robot_score}")

if player_score > robot_score:
    print("Player wins the game!")
elif player_score < robot_score:
    print("Robot wins the game!")
else:
    print("It's a tie!")