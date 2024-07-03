# # print a range of numbers
# for a in range(1,11):
#     print(a)

# # add up all the numbers from 1 - 10
# x = 0
# for n in range(1,11):
#     x += n
# print(x)

# # adding up all the odd numbers from 1 - 10
# y = 0
# for odd in range(1,11):
#     if odd % 2 != 0:
#         y += odd
# print(y)

# # adding up all the even numbers from 1 - 10
# z = 0
# for even in range(1,11):
#     if even % 2 == 0:
#         z += even
# print(z)


#reminder exercise:
num = int(input("How many times would you like to be reminded to exercise?"))

for n in range(num):
    print(f"Time {n+1}: Exercise is good. Health is Wealth")