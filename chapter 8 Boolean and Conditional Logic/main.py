# print("init")

# name = input("Enter Your name: ")
# print(name)

# if name == "Arya":
#   print("Hello Arya")
# elif name == "Snow":
#   print("Hi Snow")
# else:
#   print("Hi Andrii")

  # x = 1
  # x is 1
  # x is 0

# if 0:
#   print("hrllo")
# else:
#   print("test")
  
# if 1:
#   print("test2")
# else:
#   print("tes3")
num = 5

# if num > 1 and num < 10:
#   print("something")
# if num > 1 or num < 2:
#   print("somthing")

# from random import choice
# food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# # NO TOUCHING =============================================
# # YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# if food == 'apple' or food == 'grape':
#     print('fruit')
# elif food == 'bacon' or food == 'steak':
#     print('meat')
# elif food == 'dirt' or food == 'worm':
#     print('yuck')
# print(food)

# num = 20
# if not (num > 30 and num == 23):
#   print("success")
# else:
#   print('else')
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)         
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /



# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:    
    print("both negative")
elif x > 0 and y < 0:     
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^