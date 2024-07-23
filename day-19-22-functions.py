def make_noise():
    print("THE CROWD IS CRAZY!")
make_noise()


def square_of_7():
    return 7**2
result = square_of_7()
print(result)


#coin toss
from random import random
def coin_toss():
    if random() > 0.5:
        return "heads"
    else:
        return "tails"
print(coin_toss())


def generate_evens():
    return [x for x in range(1,50) if x%2 ==0]
print(generate_evens())


def yell(string):
    return f"{string.upper()}!"
print(yell("i am here"))

def exponent(num, power=5):
    return num ** power
print(exponent(2,6))



def return_day(num):
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    day = days.get(num)
    if day:
        return day
    return None
print(return_day(2))

#Royce attempt
def last_element(data):
    if len(data) > 0:
        return data[len(data)-1]
    return None
print(last_element([1,2,3,4,5,6,7]))

#a better, more concise version
def last_element(i):
    if i:
        return i[-1]
    return None

def number_compare(first, second):
    if first > second:
        return "First is greater"
    elif first < second:
        return "Second is great"
    return "Numbers are equal"

print(number_compare(1,10))

#royce attempt
def single_letter_count(word, letter):
    word = word.lower()
    letter = letter.lower()
    number = word.count(letter)
    if number:
        return number 
    return 0
print(single_letter_count("happy", "p"))

#better version
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
print(single_letter_count("awesome", "a"))


def multiple_letter_count(word):
    return {char:word.count(char) for char in word
    }
print(multiple_letter_count("awesome"))


def list_manipulation(alist, command, location, value=None):
    if command == "remove" and location == "end":
        return alist.pop()
    elif command == "remove" and location == "beginning":
        return alist.pop(0)
    elif command == "add" and location == "beginning":
        alist.insert(0, value)
        return alist
    elif command == "add" and location == "end":
        alist.append(value)
        return alist


print(list_manipulation([1,2,3,4,5], 'remove', 'end'))
print(list_manipulation([1,2,3,4,5], 'remove', 'beginning'))
print(list_manipulation([1,2,3,4,5], 'add', 'beginning', 10))
print(list_manipulation([1,2,3,4,5], 'add', 'end', 10))



def is_palindrome(word):
    stripped = word.replace(" ", "").lower()
    return word == word[::-1]

print(is_palindrome('tacocat'))



def multiply_even_numbers(collection):
    total = 1 
    for x in collection:
        if x%2 == 0:
            total = total * x
    return total

print(multiply_even_numbers(range(1,7)))

#alternative 1
def capitalize(word):
    return word.capitalize()

print(capitalize('japan'))

#alternative 2
def capitalize(word):
    return f"{word[0:1].upper()}{word[1:].lower()}"

print(capitalize('singapore'))


def compact(collection):
    return [x for x in collection if x]

print(compact([1,2,3,0,False, None, 'all done']))


# set & option
def intersection(collection1, collection2):
    return list(set(collection1) & set(collection2))

print(intersection([1,2,3,4,5,6], [4,5,6,7,8,11,12]))

# alternative manual looping
def intersection(collection1, collection2):
    common = []
    for x in collection1:
        if x in collection2:
            common.append(x)
    return common
print(intersection([1,2,3,4,5,6], [4,5,6,7,8,11,12]))

# list comprehension:
def intersection(collection1, collection2):
    return [x for x in collection1 if x in collection2]
print(intersection([1,2,3,4,5,6], [4,5,6,7,8,11,12]))



def is_even(num):
    return num % 2 == 0

def partition(collection, is_even):
    truthy_list = []
    falsy_list = []
    for num in collection:
        if is_even(num):
            truthy_list.append(num)
        else:
            falsy_list.append(num)
    result = [truthy_list, falsy_list]
    return result

print(partition([1,2,3,4,5,6,7,8], is_even))