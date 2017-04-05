import toolz, pyrsistent, hypothesis, effect, pytest


class User(object):
	def __init__(self, id, name, organization):
		self.id = id
		self.name = name
		self.organization = organization

	def load_from_db(store, id):
		name, org = store.find(User, id=id)
		return User(id, name, org)

	def load_owned_products(store, user_id):
		pass

	def get_email_adress(name, organization):
		return "{}@{}.org".format(name, organization)

	assert get_email_adress('name', 'organization') == "name@organization.org"
	print("OK!")


class Person(object):
	def __init__(self, name):
		self.name = name


# Recursion
class Group(object):
	"""Groups can contain Persons or more Groups."""
	def __init__(self, members, subgroups):
		self.members = members
		self.subgroups = subgroups


def get_all_members(group):
	sub_members = []
	for subgroup in group.subgroups:
		sub_members.extend(get_all_members(subgroup))
	return group.members + sub_members

group = Group(['Sam', 'Jessie'], [Group(['Reese', 'Taylor'], [])])
print(get_all_members(group))
# ~~~~~~~~~~~~~~ #


def mymap(f, l):
	if l == []:
		return l
	return [f(l[0])] + mymap(f, l[1:])

print(mymap(lambda n: n+2, [1, 2, 3]))


def biggest(nums, current_biggest=0):
	if nums == []:
		return current_biggest
	else:
		bigger = nums[0] if nums[0] > current_biggest else current_biggest
		return biggest(nums[1:], bigger)

print(biggest([1, 2, 5, 3, -1]))


# Recursive version that isn't well optimized in Python
def myreduce(f, l, acc):
	if l == []:
		return acc
	else:
		new_acc = f(l[0], acc)
		return myreduce(f, l[1:], new_acc)


# Iterative version that optimizes functions that depend upon this function
def myreduce(f, l, acc):
	for el in l:
		acc = f(el, acc)
	return acc


def biggest(l):
	return myreduce(lambda num, acc: num if num > acc else acc, l, 0)


def length(l):
	return myreduce(lambda _, acc: acc + 1, l, 0)


def mysum(l):
	return myreduce(lambda num, acc: num + acc, l, 0)


def mymap(f, l):
	return myreduce(lambda el, acc: acc + [f(el)], l, [])


def myfilter(f, l):
	return myreduce(lambda el, acc: acc + [el] if f(el) else acc, l, [])

print("Biggest", biggest([1, 2, 5, 3]))
print("Length", length([1, 2, 3, 5, 6]))
print("Sum", mysum([5, 5, 6]))
print("Add2", mymap(lambda n: n+2, [1, 2, 3]))
print("Evens", myfilter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5]))
# ~~~~~~~~~~~~~~ #


def trace(name, x, f):
	print("<{}({})>".format(name, x), end='')
	result = f(x)
	print("</{}({}): {}>\n".format(name, x, result), end='')


def trace_decorator(f):
	return lambda x: trace(f.__name__, x, f)


@trace_decorator
def doWork(x):
	return x * 2


@trace_decorator
def otherWork(x):
	return x - 5

doWork(50)
otherWork(10)
# ~~~~~~~~~~~~~~ #


class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def translate(self, x_trans, y_trans):
		# self.x = x + x_trans
		# self.y = y + y_trans
		return Point(self.x + x_trans, self.y + y_trans)
# ~~~~~~~~~~~~~~ #

from pyrsistent import pvector, v

vec = pvector([1, 2, 3])
assert vec == v(1, 2, 3)
print(vec, '\n', vec.append(4), vec.set(0, 'hello'), '\n', vec, '\n')


from pyrsistent import pmap, m

dic = pmap({'one': 'yes', 2: 0})
m(a=1, b=2)
print(dic, '\n', dic.set('one', 'yusss'), '\n', dic, '\n')


from pyrsistent import pset, s

animals = pset(['dog', 'cat', 'bird']) | s('bear', 'lion')
print(animals, '\n', animals.add('spider'), '\n', animals.remove('bird'), '\n', animals, '\n')


from pyrsistent import freeze, thaw

dic = {'sublist': [{'a', 'b', 'c'}, {'d', 'e', 'f'}]}
frozen = freeze(dic)
thawed = thaw(frozen)
print(dic, '\n', frozen, '\n', thawed, '\n')


from pyrsistent import PClass, field


class Point(PClass):
	x = field()
	y = field()

	def translate(self, x_trans, y_trans):
		return self.set(x=self.x + x_trans, y=self.y + y_trans)

p = Point(x=1, y=2)
print(p, '\n', p.translate(1, 1), '\n', p, '\n', p.serialize(), '\n')
# ~~~~~~~~~~~~~~ #

first = pvector(range(8))  # pvector([0, 1, 2, 3, 4, 5, 6, 7])
second = first.set(5, 99)  # pvector([0, 1, 2, 3, 4, 99, 6, 7])
# ~~~~~~~~~~~~~~ #


def g(x):
	return x + 10


def f(x):
	return x * 5

from toolz.functoolz import compose

compose(f, g)(3)  # 65
compose(g, f)(3)  # 25
map(compose(f, g), [1, 2, 3])  # [55, 60, 65]
map(lambda x: f(g(x)), [1, 2, 3])  # ^


from toolz.functoolz import curry


@curry
def plus(x, y):
	return x + y

plus(1, 2)  # 3
plus(1)(2)  # 3
map(plus(1), [1, 2, 3])  # [2, 3, 4]

from toolz.functoolz import identity, memoize

identity(3)  # equivalent to 'lambda x: x'


@curry
@memoize  # the return value for a given argument('s) is remembered
def minus(x, y):
	return x - y

minus(3, 4)  # -1
minus(3)(4)  # -1


from toolz.functoolz import thread_first


def inc(a): return a + 1


def double(a): return a * 2

thread_first(1, inc, double)  # 4


def add(a, n): return a + n


def mul(a, n): return a * n

thread_first(1, (add, 5), (mul, 3))  # 18
from toolz.itertoolz import nth, last, drop, take, groupby, interpose, first

nth(1, iter([1, 2, 3]))  # 2
last(iter([1, 2, 3]))  # 3

list(drop(2, iter([1, 2, 3])))  # [3]
list(take(2, iter([1, 2, 3])))  # [1, 2]
groupby(first, ['ABC', 'ABA', 'BAB', 'BAA'])  # {'A': ['ABC', 'ABA'], 'B': ['BAB', 'BAA']}
groupby(last, ['ABC', 'ABA', 'BAB', 'BAA'])  # {'A': ['ABA', 'BAA'], 'B': ['BAB'], 'C': ['ABC']}
list(interpose('meow', ['bark', 'squeal', 'bulbulbul']))  # ['bark', 'meow', 'squeal', 'meow', 'bulbulbul']

first('ABC')  # 'A'
first(iter('ABC'))  # 'A'


d1 = {'cat': 'meow'}
d2 = {'dog': 'woof'}

from toolz.dicttoolz import merge, assoc, dissoc, get_in

merge(d1, d2)  # {'cat': 'meow', 'dog': 'woof'}
assoc(d1, 'fish', 'bulbulbul')  # {'fish': 'bulbulbul', 'cat': 'meow'}
dissoc(d1, 'cat')  # {}

struct = {'a': [{'c': 'hi'}]}
print(struct['a'][0]['c'])  # 'hi'
get_in(['a', 0, 'c'], struct)  # 'hi'
get_in(['b', 0, 'c'], struct, 'not found!')  # 'not found!'
# ~~~~~~~~~~~~~~ #


def add2(num):
	return num + 2

from hypothesis import given, strategies as st


@given(st.integers())
def test_adds_2(num):
	assert add2(num) == num + 2

test_adds_2()

from operator import add


def mysum(nums):
	from functools import reduce
	return reduce(add, nums, 0)


@given(st.lists(st.integers()))
def test_mysum(nums):
	assert mysum(nums) == sum(nums)

test_mysum()


class Herd(object):
	def __init__(self, animal, number):
		self.animal = animal
		self.number = number

	def __repr__(self):
		return "<Herd of animal={} number={}>".format(self.animal, self.number)

	def __eq__(self, other):
		return (type(self) is type(other)) \
				and self.animal == other.animal \
				and self.number == other.number

animals = st.sampled_from(['moose', 'duck', 'bear', 'lion'])
print(animals.example())  # 'bear' (or something else)

herds = st.builds(Herd, animals, st.integers(min_value=0))
print(herds.example())  # '<Herd of animal=moose number=46373>' (or something else)


def parse_herd(s):
	try:
		name, num = s.split(',')
		num = int(num)
	except ValueError:
		raise SyntaxError()
	return Herd(name, num)

parse_herd('cat,10')  # '<Herd of animal=cat number=10>'


def serialize_herd(herd):
	return '{},{}'.format(herd.animal, herd.number)

serialize_herd(Herd('dog', 10))  # 'dog,10'


@given(herds)
def test_herd_roundtrip(herd):
	assert parse_herd(serialize_herd(herd)) == herd

test_herd_roundtrip()


@given(st.text())
def fuzz_herd_parser(s):
	try:
		parse_herd(s)
	except SyntaxError:
		pass

fuzz_herd_parser()


def guess_number(num):
	"Returns a message and how far away you are"
	if num == answer:
		return "You got it right!", 0
	else:
		return "Nope", answer - num

answer = 4848

from hypothesis import example


@given(st.integers())
@example(answer)
def test_guess_number(num):
	assert guess_number(num)[1] == answer - num
# ~~~~~~~~~~~~~~ #

from effect import Effect, sync_perform, sync_performer
from effect import ComposedDispatcher, TypeDispatcher, base_dispatcher
from effect.do import do


def compliment(name):
	return "Oh, {} is a lovely name~".format(name)


@do
def main():
	name = yield Effect(Input("Enter your name: "))
	yield Effect(Print(compliment(name)))


class Input(object):
	def __init__(self, prompt):
		self.prompt = prompt

	def __eq__(self, other):
		return type(self) is type(other) and self.prompt == other.prompt


class Print(object):
	def __init__(self, message):
		self.message = message

	def __eq__(self, other):
		return type(self) is type(other) and self.message == other.message


@sync_performer
def perform_input(dispatcher, intent):
	return input(intent.prompt)


@sync_performer
def perform_print(dispatcher, intent):
	print(intent.message)

# io = TypeDispatcher({
# 	Input: perform_input,
# 	Print: perform_input
# })
#
# dispatcher = ComposedDispatcher([io, base_dispatcher])
#
# if __name__ == '__main__':
# 	eff = main()
# 	sync_perform(dispatcher, eff)
# 	sync_perform(dispatcher, eff)

from effect.testing import SequenceDispatcher


def test_main():
	seq = SequenceDispatcher([
		(Input("Enter your name: "), lambda i: "woof"),
		(Print('Oh, woof is a lovely name~'), lambda i: None)
	])
	with seq.consume():
		sync_perform(ComposedDispatcher([seq, base_dispatcher]), main())

test_main()



















