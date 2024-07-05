from random import randint

print("Guess the number that I'm thinking of.")

random_num = randint(1,10)

while True:
    guess = int(input("Pick a number from 1 - 10: "))
    if guess > random_num:
        print("Too high!")
    elif guess < random_num:
        print("Too low!")
    else:
        print("You got it right!")
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == "y":
            random_num = randint(1,10)
        else:
            print("Thank you for playing. Bye~")
            break

    
