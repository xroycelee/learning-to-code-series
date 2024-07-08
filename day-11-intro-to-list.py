# creating a list:
color = ["red", "blue", "green"]

# adding items to a list
color.append("black") #add 1 item to the end of the list
color.extend(["grey", "yellow", "purple"]) #add multiple items to the end of the list
color.insert(2, "white") #add 1 item to 2nd index of list

# removing items from a list
color.pop() #remove last item in list + return the value
color.pop(3) #remove 3rd index item in list
color.remove("red") #remove the first instance of the item "red"
color.clear() #empties the whole list

# accessing data in list
my_favourite = color[1]
print(my_favourite)

# checking if item exists in list
if "white" in color:
    print("That's my favourite color too!")
