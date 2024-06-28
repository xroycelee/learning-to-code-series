print("Hi! Welcome to the oz calculator")

print("What indgredient are you using?")
ingredient = input()

print("How many oz do you need?")
oz = input()
oz = int(oz)

grams = (oz*28.3495)
grams = round(grams, 2)

print(f"You will need {grams}grams of {ingredient}")