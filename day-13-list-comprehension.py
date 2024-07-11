num = list(range(1,11))

#------ multiply numbers by 10 -----
# with list comprehension
multiplied = [n*10 for n in num]
print(multiplied)

# without list comprehension
multiplied = []
for n in num:
    n = n*10
    multiplied.append(n)
print(multiplied)

#------ multiply EVEN numbers by 10 -----
# with list comprehension
even_multiplied = [n*10 for n in num if n%2 == 0]
print(even_multiplied)

# without list comprehension
even_multiplied = []
for n in num:
    if n%2 == 0:
        n = n*10
        even_multiplied.append(n)
print(even_multiplied)