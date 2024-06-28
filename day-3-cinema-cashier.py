# < 13 come back with your parents
# 13 - 21 student, pay student price
# 21 - 65  adult, pay adult price
# 65+  senior, free

print("Welcome to the cinema!")
print("What is your age?")
age = input()
age = int(age)

if age < 13:
    print("You're too young! Come back with your parents.")
elif age >= 13 and age < 21:
    print("You're a student, please pay student price: $6.")
elif age >= 21 and age < 65:
    print("You're an adult, please pay adult price: $12.")
else:
    print("You're a senior, it's free for you.")