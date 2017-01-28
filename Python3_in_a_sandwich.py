# coding=utf-8
""" A .py file showing various important parts of Python as well as those that are just cool :3
pep8 line length set to 120, not the standard 79.
    I recommend testing various parts of this file at http://www.pythontutor.com/visualize.html
it will give you a visual explanation of each step that happens behind the scenes """
#
#
######################


""" Raw strings """
#
#
# This string ends in a newline
print("Hello!\n")
#
# This string ends in a backslash followed by an 'n'
print(r"Hello!\n")
#
#
###########################

""" lists """
#
#
# append several values at once to the end
numbers = [6, 10, 42]
numbers.extend([666, 1337, 9001])
#
# insert a value at a particular index
numbers.insert(0, 7)  # insert 7 at the beginning of the list
#
# remove an element by its index and assign it to a variable, default popped index is -1
my_number = numbers.pop(2)
#
# This creates a week calendar
timetable = [[""] * 24 for day in range(7)]
#
#
###########################


""" sets """
#
#
# this is an empty dictionary
a = {}
#
# this is how we make an empty set
b = set()
#
#
############################


""" dictionary """
#
#
Pokéballs = {"Poké Ball": 64, "Great Ball": 30, "Ultra Ball": 31, "Safari Ball": 29}
#
# Get a value by its key, or None if it doesn't exist
Pokéballs.get("Master Ball")
# We can specify a different default
Pokéballs.get("Master Ball", 1)
#
# Add several items to the dictionary at once
Pokéballs.update({"Great Ball": 20, "Ultra Ball": 30, "Safari Ball": 12})
#
# All the keys in the dictionary
Pokéballs.keys()
# All the values in the dictionary
Pokéballs.values()
# All the items in the dictionary
Pokéballs.items()
#
colours = list(Pokéballs)  # the keys will be used by default
counts = tuple(Pokéballs.values())  # but we can use a view to get the values
Pokéballs_set = set(Pokéballs.items())  # or the key-value pairs
#
#
#############################


""" errors """
#
#
# causing an error (best if expected) to show up with a custom print++


class MySpecialError(ZeroDivisionError):
    pass
#
try:
    something = 1 / 0  # I am causing a random error
except ZeroDivisionError as zero_div_error:
    print("Error class is: ", type(zero_div_error))
    print("Going deeper..")
    try:
        print("I am a bad thing that needs to be tested ;>")
        raise MySpecialError("[Informative things]")
    except MySpecialError:
        print("Thank youuuuuu~")
#
#
#############################


""" logging """
#
#
import logging
#
# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='my_program.log', level=logging.ERROR)
#
# these messages should appear in our file
logging.error("There's a spider on your head!")  # ERROR – for less serious errors
logging.critical("The cat is on fire!")  # CRITICAL – for very serious errors
#
# but these ones won't
logging.warning("We're almost out of pineapple juice.")  # WARNING – for warnings
logging.info("It's rainy today.")  # INFO – for important informative messages
logging.debug("I had my medicine for breakfast.")  # DEBUG – for detailed debugging messages
#
#
try:
    age = int(input("How old are you? "))
except ValueError as err:
    logging.exception(err)  # logging level: ERROR
#
#
###############################


""" try...except...else...finally """
#
#
try:
    age = int(input("Please enter your age: "))
    if age < 0:
        raise ValueError("%d is not a valid age. Age must be positive or zero.")
except ValueError as err:
    print("You entered incorrect age input: %s" % err)
else:
    print("I see that you are %d years old." % age)
finally:
    print("I like your style kiddo, welcome!")
#
#
###############################


""" *args & **kwargs """
#
#
# names args and kwargs that aren't important, but the */** characters preceding them are
#


def catch_all(*args, **kwargs):  # *<var_name> means "expand this as a sequence"
    print("args =", args)        # **<var_name> means "expand this as a dictionary"
    print("kwargs = ", kwargs)
#
catch_all(1, 2, 3, a=4, b=5)
# args = (1, 2, 3)
# kwargs = {'a': 4, 'b': 5}
#
# this syntax can not only be used with the function definition but with the function call as well!
inputs = (1, 2, 3)
keywords = {'pi': 3.14}
catch_all(*inputs, **keywords)
# args = (1, 2, 3)
# kwargs = {'pi': 3.14}
#
#
#############################


""" lambda functions """
#
#
# defining short, one-off functions is possible with the lambda statement
add = lambda x, y: x + y  # it's roughly equivalent to def add(x, y):
add(1, 2)                                                 # return x + y
# 3
#
# everything is an object in Python, even functions themselves! So even functions can be passed as args to functions
#
#
#############################


""" Iterators """
#
#
iter([2, 4, 6, 8, 10])
# <list_iterator at mem_location > is printed
"""It is this iterator object that provides the functionality required by
the for loop. The iter object is a container that gives you access to
the next object for as long as it’s valid, which can be seen with the
built-in function next"""
I = iter([2, 4, 6, 8, 10])
print(next(I))
# 2
print(next(I))
# 4
print(next(I))
# 6
# Python can treat other things as lists due to the way iterators work here
# range() is an example of this. It isn't a list but a special object!
#
iter(range(10))
# <range_iterator at mem_location> is printed
#
# since an iterator is a great example of the lazy part of programming
# languages it creates as many things as you tell it to one by one.
#
#
" enumerate "
#
# enumerate is a fantastic example of an iterator:
list_x = [2, 4, 6, 8, 10]
for index_of_list_x in range(len(list_x)):
    print(index_of_list_x, list_x[index_of_list_x])
# the code above works, but the cleaner version of this is simply:
for index_of_list_x, value_of_the_current_index in enumerate(list_x):
    print(index_of_list_x, value_of_the_current_index)
#
#
" zip "
#
L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
for lval, rval in zip(L, R):
    print(lval, rval)
# 2 3
# 4 6
# 6 9
# 8 12
# 10 15
#
# Any number of iterables can be zipped together, and if they are different lengths, the shortest
#   will determine the length of the zip.
#
# ponder this for a while
L1 = (1, 2, 3, 4)
L2 = ('a', 'b', 'c', 'd')
#
z = zip(L1, L2)
print(*z)
# (1, 'a') (2, 'b') (3, 'c') (4, 'd')
new_L1, new_L2 = zip(*z)
print(new_L1, new_L2)
# (1, 2, 3, 4) ('a', 'b', 'c', 'd')
# If you understand why this works you really do get iterators!
# Now, the zip function can cause unexpected situations due to the way it determines the length by the shortest
#   iterable. If this behaviour is something you want to avoid, there is an alternative called zip_longest:
from itertools import zip_longest
L1 = (1, 2, 3, 4, 5, 6, 7)
L2 = ('a', 'b', 'c', 'd')
z = zip_longest(L1, L2)
print(*z)
# (1, 'a') (2, 'b') (3, 'c') (4, 'd') (5, None) (6, None) (7, None)
#
#
" map "
#
square = lambda x: x ** 2  # (Such a way of creating functions should be avoided, here it's just for demonstration)
for val in map(square, range(10)):  # the map iterator takes a function and applies it to the values
    print(val, end=' ')               # in an iterator
# 0 1 4 9 16 25 36 49 64 81   # find the title 10 square numbers
#
print(*map(lambda x: x ** 2, range(10)))  # this does exactly the same thing as the example above
#
#
" filter "
#
# find values up to 10 for which x % 2 is zero
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):  # The filter iterator only passes through values for which
    print(val, end=' ')                   # the filter function evaluates to True
# 0 2 4 6 8
#
#
" specialized iterators: itertools "
#
# the itertools module contains a ton of useful iterators: https://docs.python.org/3/library/itertools.html
#  here are some examples:
#
from itertools import permutations  # the itertools.permutations function iterates over all permutations of a sequence:
p = permutations(range(3))
print(*p)
# (0, 1, 2) (0, 2, 1) (1, 0, 2) (1, 2, 0) (2, 0, 1) (2, 1, 0)
#
from itertools import combinations  # the itertools.combinations function iterates over all unique combinations of N
c = combinations(range(4), 2)        # values within a list:
print(*c)
# (0, 1) (0, 2) (0, 3) (1, 2) (1, 3) (2, 3)
#
from itertools import product  # the itertools.product function iterates over all sets of pairs between two or more
p = product('ab', range(3))     # iterables:
print(*p)
# ('a', 0) ('a', 1) ('a', 2) ('b', 0) ('b', 1) ('b', 2)
#
#
##############################


""" list comprehensions """
#
#
# Lets start with an example:
L = []
for val in range(20):  # The result of this is a list of numbers that exclude multiples of 3.
    if val % 3:
        L.append(val)
L
# [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
#
# List comprehensions are simply a way to compress a list-building for loop into a single short, readable line.
# Here's an example that compares two ways of making a list that consists of the title 12 square integers:
L = []
for n in range(12):
    L.append(n ** 2)
L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
#               vs...
[n ** 2 for n in range(12)]  # means "construct a list consisting of the square of n for each n up to 12"
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
#
# So the basic syntax is: [expr for var in iterable], where expr is any valid expression, var is a variable name and
#                                                                             iterable is any iterable Python object.
#
# You can further control the iteration by adding a conditional to the end of the expression as in the title example.
[i for i in range(20) if i % 3 > 0]
# [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
# This can be read as "construct a list of values for each value up to 20, but only if the value is not divisible by 3"
#
# Furthermore you can have multiple iterations by adding another iterators within the comprehension:
[(i, j) for i in range(6) for j in range(7) if i % 2 > 0 and j % 3 == 0]  # This is, however, quite unreadable!
# [(1, 3), (1, 6), (3, 0), (3, 3), (3, 6), (5, 0), (5, 3), (5, 6)]
#
#
##############################


""" conditionals on the value """
#
#
# single line conditionals are great when a simple expression is desired.
#
[val if val % 2 else -val              # all multiples of 2 will be negated within the list...
    for val in range(20) if val % 3]    # ...which consists of numbers in the given range excluding multiples of 3.
# [1, -2, -4, 5, 7, -8, -10, 11, 13, -14, -16, 17, 19]
#
# the braces of the iterator have a meaning:
{a % 3 for a in range(1000)}  # set will be made here
# {0, 1, 2}
# but what is inside is as important:
{n: n**2 for n in range(6)}  # and here a dictionary will be made
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# finally by using parentheses rather than square or curly braces you get the generator expression:
(n**2 for n in range(12))
# < generator object <genexpr> at mem_location>
#
#
##############################


""" generators """
#
#
# main difference in code between comprehensions and generators is the type of braces around the expression:
[n**2 for n in range(12)]  # list comprehension
#  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
{n**2 for n in range(12)}  # dictionary comprehension
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121}
(n**2 for n in range(12))  # generator expression
# < generator object <genexpr> at mem_location>
#
# by passing the generator expression to the list constructor we can print its work
G = (n**2 for n in range(12))
list(G)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
#
# main difference between a list and a generator is that while lists build a collection of values that are stored in
# memory, generators are just a recipe for making those values. Generators are the lazy part of Python, they only do
# their job if you tell them to, so they are not only memory and computationally efficient but also they are unlimited!
# But there is a catch, a list can be iterated multiple times; a generator expression is single use:
L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')
print()
# 0 1 4 9 16 25 36 49 64 81 100 121
for val in L:
    print(val, end=' ')
# 0 1 4 9 16 25 36 49 64 81 100 121
# yet if you try this with the generator:
G = (n ** 2 for n in range(12))
list(G)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
list(G)
# []
# We can use this property to do something very useful like for example:
G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30:
        break
print("\nsomething in between")
for n in G:
    print(n, end=' ')
# 0 1 4 9 16 25 36
# something in between
# 49 64 81 100 121
#
#
" generator functions "
#
#
# ///////WIP/////////
##############################


""" important notes """
#
#
"encoding and decoding functions for 'str' and 'bytes'"
# In Python 3.x there are two types used for sequences of characters: bytes, which contain raw 8-bit values,
# and str, that contain Unicode characters. The core of your program should use Unicode character types and should
# not assume anything about the encodings. This way you can with ease accept other text encodings (Big5, Latin-1, etc.)
# while being strict about the encoding of your output (utf-8).


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes
#
# Another thing to remember is that the file handlers (open function) default to utf-8 encoding in Python 3.
# That means that when you want to write binary data to a file you should use 'wb' instead of 'w', etc. An example:
import os
with open('/tmp/random.bin', 'wb') as f:
    f.write(os.random(10))
# If 'w' was used instead a TypeError would happen.
#
#
##############################


""" cool stuff really aka various examples """
#
#


def my_insides():
    sam = "Jolly Boy"
    twist = 1.34
    return locals()  # {'sam': 'Jolly Boy', 'twist': 1.34}


def sam_how_are_you():
    sam = 'Been better'
    return locals()['sam']  # 'Been better'
# You can do the same thing with globals() which returns the global variables!
#
#
person = {}

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

for property, p_type in properties:
    valid_value = None

    while valid_value is None:
        try:
            value = input("Please enter your %s: " % property)
            valid_value = p_type(value)
        except ValueError as ve:
            print("Could not convert {} '{}' to type {}.".format(property, value, p_type.__name__))
            raise ve

    person[property] = valid_value
#
#
# # # # # # # # # # # # # # # #
#
#
data = [{'title': 'The Legend of Zelda', 'publisher': 'Nintendo', 'RD': 1986},
        {'title': 'Chrono Trigger', 'publisher': 'Square', 'RD': 1995},
        {'title': 'Ōkami', 'publisher': 'Capcom', 'RD': 2006}]
# sort alphabetically or numerically by value in given key
data_by_release = sorted(data, key=lambda item: item['RD'])
print(data_by_release)
# [{'RD': 1986, 'publisher': 'Nintendo', 'title': 'The Legend of Zelda'},
#  {'RD': 1995, 'publisher': 'Square', 'title': 'Chrono Trigger'},
#  {'RD': 2006, 'publisher': 'Capcom', 'title': 'Ōkami'}]
#
#
# # # # # # # # # # # # # # # #
#
# You can  set terminal to desired size by print("\x1b[8;<height>;<width>t") at the beginning of the program
# where <height> and <width> are values
#
#
# # # # # # # # # # # # # # # #


def is_isogram(string):
    return len(string) == len(set(string.lower()))
#
#
# # # # # # # # # # # # # # # #
#
#
" Tuple unpacking "
#
l = [(2, 4), (6, 8), (10, 12)]
for tup in l:
    print(tup)
# (2, 4) (6, 8) (10, 12)
# Now with unpacking!
for (t1, t2) in l:
    print(t1)
# 2 6 10
#
#
###########################

"""
    Inspired and heavily influenced by the book "A Whirlwind Tour of Python" by Jake VanderPlas.
    The 'important notes' section is mostly a loose copy of fragments of the book "Effective Python: 59 Specific Ways
        to Write Better Python" by Brett Slatkin.
    Some parts were provided by the wonderful Stackoverflow community
                                                                        """
