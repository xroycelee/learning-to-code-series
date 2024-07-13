# length function
num = list(range(10))
print(len(num)) # indicates how many items are in the list

# index function
print(num.index(1, 2)) # to find the index of the mentioned item - '1' within the list starting from 2nd index onwards

# count function
print(num.count(2)) #to find out how many instances the item appears in the list

# sort function
num.sort() # sort the list

# reverse function
num.reverse() # reverse the list

# join function
counting = "...".join(str(num))
print(f"I am counting! {counting}")

# slicing
number = list(range(20))
print(number[1::2]) # starting from index #1, and increasing by steps of 2

# iterating over lists (like loops)
# example 1
for n in list(range(5)):
    print(n) # 1, 2, 3, 4

# example 2
for n in [1, 2, 3, 4]:
    print(n) # 1, 2, 3, 4

# example 3
color = ["red", "blue", "orange", "black"]
i = 0 # index of item in list
while i < len(color):
    print(f"color {i+1}: {color[i]}")
    i += 1