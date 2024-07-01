# welcome to the game of rock, paper, scissors
# Player 1 please pick your move
# Player 2 please pick your move

#draw
# rock > scissors
# scissors > paper
# paper > rock

print("Welcome to the game of rock, paper, scissors")
player_1 = input("Player 1 please pick your move: ").lower()
player_2 = input("Player 2 please pick your move: ").lower()

if player_1 == player_2:
    print("It's a draw!")
elif player_1 == "rock":
    if player_2 == "scissors":
        print("Player 1 wins!")
    elif player_2 == "paper":
        print("Player 2 wins!")
elif player_1 == "paper":
    if player_2 == "rock":
        print("Player 1 wins!")
    elif player_2 == "scissors":
        print("Player 2 wins!")
elif player_1 == "scissors":
    if player_2 == "paper":
        print("Player 1 wins!")
    elif player_2 == "rock":
        print("Player 2 wins!")
else:
    print("Opps, something went wrong! Only pick 'rock', 'paper', 'scissors'.")