# dictionary + access data
person = {"name": "royce", "location": "earth", "race": "human"}
print(person["name"])
print(person["location"])

#iterating over dictionary. key value pair
#key option 1:
for k in person:
    print(k)
# key option 2:
for k in person.keys():
    print(k)
#value
for v in person.values():
    print(v)
#items
for k,v in person.items():
    print(f"key is {k},value is {v}")


#shopping list
from random import choice

item = choice(["fish", "chicken", "milk", "egg", "plants", "watermelon", "apple", "pear", "muffins", "rice"])

shopping_list = {
    "fish": 3,
    "chicken": 4,
    "milk": 2,
    "egg": 12
}

print(f"{item} is here!")

# using IN function
if item in shopping_list:
    print(f"I need {shopping_list[item]} {item}")
else:
    print("I do not need this")

# using .get()
quantity = shopping_list.get(item)
if quantity:
    print(f"I need {quantity} {item}")
else:
    print("I do not need this")