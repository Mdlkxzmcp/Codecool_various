import random


class Animal(object):

    def __init__(self, age=0):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name="none yet"):
        self.name = new_name

    def __str__(self):
        return "animal: {}: {}".format(self.name, self.age)


class Cat(Animal):

    def speak(self):
        print("meow")

    def __str__(self):
        return "cat: {}: {}".format(self.name, self.age)


class Rabbit(Animal):

    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def speak(self):
        print("meep")

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
            and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

    def __str__(self):
        return "rabbit: {}: {}".format(self.name, self.age)


class Person(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        if self.age > other.age:
            print("{} is {} years older than {}.".format(self.name, diff, other.name))
        else:
            print("{} is {} years younger than {}.".format(self.name, diff, other.name))

    def __str__(self):
        return "person: {}: {}".format(self.name, self.age)


class Student(Person):

    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()

        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("Let's hang")

    def __str__(self):
        return "student: {}: {}: {}".format(self.name, self.age, self.major)
