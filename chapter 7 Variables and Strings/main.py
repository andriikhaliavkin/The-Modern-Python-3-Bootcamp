# print("init")
# x = 100
# print(x)
# n = "some text"
# print(n)
# d = True
# print(d)
# x = d
# print(x)
# q, w, e = 1, 2, 3
# r = q + w + e
# print(r)

# list_example = [1, 2, 4]
# dict_example = {"a": 2, "b": 4}

# None #like null in another PLs
# name = None
# print(name)

# message = "bla bld\n"
# mountains = "/\\/\\/\\"
# print(mountains)

# name = "Andrii"
# last_name = "Khaliavkin"
# print(name + " " + last_name)
# print(f"{name} {last_name}")

# char = "qwertt"[0]
# print(char)


# decimal = 12.343
# integer = int(decimal)
# print(integer)

# my_list = [1, 2, 3]
# my_list_as_a_string = str(my_list)
# print(my_list_as_a_string)


# print("How many kms did U cycle today?")
# kms = float(input())
# miles = kms/1.60934
# print(f"OK, You said {round(miles,2)} miles")

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
while number != 5:
    number = randint(1,10)
    i += 1
print(i)
