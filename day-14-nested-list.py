# list comprehension:
[num for num in range (1,4)]

#nested list:
[[num for num in range(1,4)] for n in range(1,4)]

# schedule for the week - monday, tuesday, wednesday, thursday, friday
week = [['eat', 'sleep', 'play'], ['grocery', 'meal prep', 'swim'], ['read', 'sleep', 'nap'], ['eat', 'study', 'run'], ['sports', 'music', 'study']]

# to print what I have to do each day:
print("This is my schedule for Mon - Fri")
for n in week:
    print(n)

# to access particular data within the nested list:
a = week[0][1] # monday, 2nd activity
print(a)
b = week[3][-1] # thursday, last activity
print(b)