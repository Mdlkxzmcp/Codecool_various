# coding=utf-8
""" A .py file showing various important parts of Python as well as those that are just cool!
pep8 line length set to 120, not the standard 79.
    I recommend testing various parts of this file at http://www.pythontutor.com/visualize.html
it will give you a visual explanation of each step that happens behind the scenes
    More information can be found at the bottom of the file. This is still a WIP, and as such doesn't include proper
annotations regarding sources. Final version will be a .ipynb file.
    For best visual experience use Monokai Seti. """
#
#
######################


""" raw strings """
#
#
# This string ends in a newline
print("Hello!\n boo!")
# Hello!
#  boo!
# This string ends in a backslash followed by an 'n'
print(r"Hello!\n boo")
# Hello!\n boo
#
# There are also ways to format values into strings.
from math import pi
# The simplest way is to find the string representation:
"The value of pi is " + str(pi)
# 'The value of pi is 3.141592653589793'
#
# That technique is quite limitting though, thankfully we can use special format method:
"The value of pi is {}".format(pi)
# 'The value of pi is 3.141592653589793'
#
"The value of pi is {1:.3f}; my lucky number is {0}".format(8, pi)  # where 1 and 0 refer to the index of the value
# 'The value of pi is 3.142; my lucky number is 8'                  # and the .3f encodes the desired precision
#
"First: {last}. Last: {first}.".format(last="first", first="last")
# 'First: first. Last: last.'
#
#
###########################


""" Regular Expressions and such """
#
#
line = 'the quick brown fox jumped over a lazy dog'
# Searching for the index of the first occurence of a char or substring:
line.find('fox')
# 16
line.find('duck')  # If the char/substring isn't present
# -1
# You can also do this from the right side:
line.rfind('a')
# 35
line.startswith('lazy')
# False
line.endswith('dog')
# True
# If you want to replace all of the occurences of the given input:
line.replace('lazy', 'gigantic')  # this returns a new string v
# 'the quick brown fox jumped over a gigantic dog'
"splitting and partitioning"
# You can partition a string into a tuple with partition():
line.partition('fox')
# ('the quick brown', 'fox', 'jumped over a lazy dog')
# Just like with find, there is a rpartition() that searches form the right.
# Splitting is done with the split(), in case of the need of splitting lines there is splitlines()
# There is also the opposite of split() in a sense -> join()
'-+-'.join(['5', '6', '7'])
# '5-+-6-+-7'
#
# This is great and all, but the real power comes with 'regular expressions'.
import re
regex = re.compile('\s+')  # \s is a special character that matches any whitespace, and the + indicates mach one or more
regex.split(line)
# ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'a', 'lazy', 'dog']
# regex has some methods that are really similar to str methods:
line.index('fox')
# 16
regex = re.compile('fox')
match = regex.search(line)
match.start()
# 16
#
line.replace('fox', 'BEAR')
# 'the quick brown BEAR jumped over a lazy dog'
regex.sub('BEAR', line)
# 'the quick brown BEAR jumped over a lazy dog'
#
# despite some similar methods and such, regular expressions support way more complex ways of doing things:
email = re.compile('\w+@\w+\.[a-z]{2}')
text = "To email Lord Cheesecake, try lord@cheesecake.jp or the older address sir.mighty@cheesecake.jp."
email.findall(text)
# ['lord@cheesecake.jp', 'mighty@cheesecake.jp']
email.sub('--@--.--', text)
# 'To email Lord Cheesecake, try --@--.-- or the older address sir.--@--.--.'
# regular expressions are strict though:
email.findall('barack.obama@whitehouse.gov')
# ['obama@whitehouse.go']
#
# you can match special characters by escaping them with a backslash when using a raw string:
regex = re.compile(r'\$')
regex.findall("the cost is $20")
# ['$']
#
# said special characters within regular expressions are:
# . ^ $ * + ? { } [ ] \ | ( )
#
# otherwise backslash makes some characters 'special markers'. Here are some:
# \d - digit
# \D - non-digit
# \s - whitespace
# \S - non-whitespace
# \w - alphanumeric char
# \W - non-alphanumeric char
regex = re.compile(r'\w\s\w')
regex.findall('the fox is 9 years old')
['e f', 'x i', 's 9', 's o']
#
# square brackets match groups of custom characters:
regex = re.compile('[aeiou]')
regex.split('incompetent')
# ['', 'nc', 'mp', 't', 'nt']
#
# dash is used to specify a range:
regex = re.compile('[c-t][1-6]')
regex.findall('gf65s2cc9i4, l2l3s00G4')
# ['f6', 's2', 'i4', 'l2', 'l3']
#
# curly brackets with a number represent a repetition:
regex = re.compile(r'\w{3}')
regex.findall(line)
# ['the', 'qui', 'bro', 'fox', 'jum', 'ped', 'ove', 'laz', 'dog']
#
# other repetition markers for regex:
# ?      - zero or one
# *      - zero or more
# +      - one or more
# {n}    - n repetitions
# {m, n} - between m and n repetitions
#
email = re.compile('[\w.]*@\w+\.[a-z]{2,3}')
email.findall('barack.obama@whitehouse.gov')
# ['barack.obama@whitehouse.gov']
#
# parentheses indicate groups to extract:
email = re.compile('([\w.]*)@(\w+)\.([a-z]{2,3})')
email.findall(text)
# [('lord', 'cheesecake', 'jp'), ('sir.mighty', 'cheesecake', 'jp')]
#
# it is also possible to name the extracted components:
email = re.compile('(?P<user>[\w.]*)@(?P<domain>\w+)\.(?P<suffix>[a-z]{2,3})')
match = email.match('lord@cheesecake.jp')
match.groupdict()
# {'domain': 'cheesecake', 'suffix': 'jp', 'user': 'lord'}
#
#
##############################


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
# This is how we make an empty set
a_set = set()
# Now what can we do with sets?:
# Add a value to it
a_set.add(3)
# Note that only a single argument can be passed here
a_set.add(3)
# Only unique values are stored
a_set
# {3}
# Clear the set so it's empty
a_set.clear()
a_set = {2, 5, 9, 21}
# Copy the set to a new set
copy_set = a_set.copy()
# Now both sets have the same insides but a modification to a_set won't affect copy_set
a_set.add(111)
# Return the difference between two sets
a_set.difference(copy_set)
# {111}
# Return the first set after removing elements in the passed set
a_set.difference_update(copy_set)
a_set
# {111}
# Discard an element from a set if it is a member, otherwise this does nothing
copy_set.discard(5)
#
# Now for something a tad different:
supreme = {1, 2, 4, 5, 6}
albatros = {1, 3, 5}
# Return the intersection of two or more sets as a new set, .intersection_update exists
supreme.intersetion(albatros)
# {1, 5}
# Return a boolean value, True if two sets have a null intersection, False otherwise
supreme.isdisjoint(albatros)
# False
peanut = {1, 3}
# Return whether the first set is contained in the other
peanut.issubset(albatros)
# True
# Retrun whether the first set contains the passed one
peanut.issuperset(albatros)
# False
# Return a symmetric difference of two sets as a new set, .symmetric_update exists
supreme.symmetric_difference(albatros)
# {2, 3, 4, 6}
# Return the union of two sets
supreme.union(peanut)
# {1, 2, 3, 4, 5, 6}
# Update a set with the union of itself with others
peanut.update(supreme)
peanut
# {1, 2, 3, 4, 5, 6}
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
# When a more complicated generator is needed, generator functions are where it's at.
G1 = (n ** 2 for n in range(12))


def gen():
    for n in range(12):
        yield n ** 2  # Instead of using return like in normal functions, here we call yield to yield a sequence
G2 = gen()
print(*G1)
# 0 1 4 9 16 25 36 49 64 81 100 121
print(*G2)
# 0 1 4 9 16 25 36 49 64 81 100 121
# Main difference here is that even though the state of both of the generators is saved between partial iterations
# the function can be simply called again.
#
# < W I P >
##############################


""" collections module """
#
#
# The collections module is a built-in implementation of additional specialized container data types:
import collections as col
#
#
"Counter"
# Counter is a dictionary subclass that stores elements as keys and counts of the objects as the value.
letters = "somebodyoncetoldmepleasetakeashoweryeahrightsureeeee"
counted_letters = col.Counter(letters)
counted_letters
# Counter({'e': 13, 'o': 5, 'a': 4, 's': 4, 't': 3, 'r': 3, 'h': 3, 'y': 2, 'l': 2, [...], 'w': 1})
counted_letters.most_common(3)
# [('e', 13), ('o', 5), ('a', 4)]
# Other common uses of Counter include .clear(), .items(), .most_common()[:-n-1:-1] for n least common elements, etc.
#
#
"defaultdict"
# A dictionary-like object which extends the dictionary with a special first argument (default_factory), which sets
# the default data type for the dictionary. A defaultdict will never raise a KeyError due to this!
def_dict = col.defaultdict(lambda: 1337)
def_dict['shazam']
# 1337
#
#
"OrderedDict"
# A special dictionary subclass that stores the contents in the order in which they were added
ord_dict1 = col.OrderedDict()
ord_dict1['one'] = 1
ord_dict1['two'] = 2
ord_dict2 = col.OrderedDict()
ord_dict2['two'] = 2
ord_dict2['one'] = 1
# If those were normal dictionaries the statement below would be True
ord_dict1 == ord_dict2
# but here it evaluates to False!
#
#
"namedtuple"
# The most unique of the bunch, namedtuple assigns both names (which is the special feature) and indexes to each member:
Movie = col.namedtuple('Movie', 'title year length')
# You might sense what is comming, namedtuple allows for a very quick creation of new objects/classes!
Space_Jam = Movie(title='Space Jam', year=1996, length='1h 28min')
A_Scanner_Darkly = Movie(title='A Scanner Darkly', year=2006, length='1h 40min')
Space_Jam.year  # Our tuples gain attributes!
# 1996
Space_Jam[1]  # while still being 'standard' tuples
# 1996
#
#
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
"creating copies"
# By using the copy module we gain the ability to make two types of copies: shallow ones and deep ones:
import copy
things = [1, 2, [3]]
things_shallow = copy.copy(things)
things_deep = copy.deepcopy(things)
#
#
##############################


""" cool stuff really aka various examples and such """
#
#
# If you want to reference to the last value you can use '_' instead of it's name:
2 + 1
# 3
_ + 2
# 5
#
#
# # # # # # # # # # # # # # # #
#
#
# There is this cool thing called bit shifting:
17 >> 1  # shift to the right by one, << shifts to the left
# 8
# since 17 in base 2 is 10001 when we shift it to the right by one we get 1000
#
#
# # # # # # # # # # # # # # # #
#
#


def my_insides():
    sam = "Jolly Boy"
    twist = 1.34
    return locals()
# {'sam': 'Jolly Boy', 'twist': 1.34}


def sam_how_are_you():
    sam = 'Been better'
    return locals()['sam']
# 'Been better'
# You can do the same thing with globals() which returns the global variables!
#
#
# # # # # # # # # # # # # # # #
#
#
"fun with numbers~"
# besides the boring float, int and whatnot you can also make hexadecimal and binary numbers with ease!
hex(659)
# '0x293'
bin(62)
# '0b111110'
#
# You can also right-pad a string (usually a number) with zeros:
'256'.zfill(10)
# '0000000256'
#
#
# # # # # # # # # # # # # # # #
#
#
# a random prime generator out of nowhere!


def gen_primes(N):
    primes = set()
    for num in range(2, N):
        if all(num % p > for p in primes):
            primes.add(num)
            yield num
#
#
# # # # # # # # # # # # # # # #
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
#
#


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
