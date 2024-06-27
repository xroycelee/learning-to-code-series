print("Hi! Welcome to the oz calculator")

print("What indgredient are you using?")
ingredient = input()

print("How many oz do you need?")
oz = input()
oz = int(oz)

amount_in_grams = int(oz*28.3495)

print(f"You will need {amount_in_grams}grams of {ingredient}")