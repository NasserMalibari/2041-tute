#!/usr/bin/env python3

'''
Warning: 

There is no guarantee that this file makes sense out
of context.
'''


import timeit

def comp():
    a = [i**2 for i in range(10000)]

def loops():
    a = []
    for i in range(10000):
        a.append(i**2)


def map_example_comp():
    add_2 = [(num + 2) for num in range(100)]

def map_example():
    add_2 = list(map(lambda x: x+2, range(1000)))
    # print(type(add_2))

list_comp_times = timeit.timeit(map_example_comp, number = 10000)
print(list_comp_times)

list_comp_times = timeit.timeit(map_example, number = 10000)
print(list_comp_times)

# reduce -> import functools

# list comprehensions

# [1,4,9,...]

def square_nums():
    squares = []
    for num in range(15):
        squares.append(num**2)
    print(squares)


def square_nums_comps():
    # square_nums = [(computation) for num in (iterable)]
    square_nums = [num**2 for num in range(15)]
    print(square_nums)

def square_nums_conditional():
    # square_nums = [(computation) for num in (iterable) *if (expr)*]
    square_nums = [num**2 for num in range(15) if num % 2 == 0]
    print(square_nums)




# square_nums_conditional()

words = ["foo", "bar", "alpha", "gamma"]
# -> ["f", "b", "a", "g"]

first_letters = []
for word in words:
    first_letters.append(word[0])

# [(computation) for num in (iterable)]
first_letters_comp = [word[0] for word in words]
# print(first_letters_comp)

# ["foo", "bar"] -> ["f","b"]
# list(map(...)) 








# times = timeit.timeit(comp, number = 10000)

# print(times)

# times = timeit.timeit(loops, number = 10000)
# print(times)

# comp_times = timeit.timeit(map_example_comp, number=10000)
# print(comp_times)

# comp_times = timeit.timeit(map_example, number=10000)
# print(comp_times)
