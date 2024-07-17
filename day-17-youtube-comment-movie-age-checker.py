# Make a list of 10 movies, with age ranges (13+ 18+,)
# select a movie, 
# then provide the age 
# tells me if i'm old enough to view the movie

from random import choice 

movies = [
    ['Frozen', 13],
    ['The Avengers', 13],
    ['Inception', 13],
    ['The Hunger Games', 13],
    ['The Dark Knight', 18],
    ['Pulp Fiction', 18],
    ['Fight Club', 18],
    ['Deadpool', 18],
    ['Blue is the Warmest Colour', 21],
    ['Shame', 21]
]

watch = choice(movies)
print(f"The movie that you will be watching is: {watch[0]}")
age = int(input("Before I can let you in, I need to know your age. How old are you?"))

if age > watch[1]:
    print("You're all good to go, enjoy the movie")
else:
    print(f"You're too young, you need to be {watch[1]} years old to watch this movie. Please come back with your parents")