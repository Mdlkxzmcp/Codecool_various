#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 18:57:05 2017

@author: mdlkxzmcp
"""

class Person(object):

    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):

    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):

    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)


class ArrogantProfessor(Professor):

    def say(self, stuff):
        return 'It is obvious that ' + self.say(stuff)
    


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')


e.say('the sky is blue')
le.say('the sky is blue')
le.lecture('the sky is blue')
pe.say('the sky is blue')
pe.lecture('the sky is blue')

# 6-1
class ArrogantProfessor(Professor):

    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)
# >>> ae.say('the sky is blue')
# eric says: It is obvious that eric says: the sky is blue

# >>> ae.lecture('the sky is blue')
# It is obvious that eric says: the sky is blue

# 6-2
class ArrogantProfessor(Professor):
    
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
# >>> ae.say('the sky is blue')
# eric says: It is obvious that I believe that eric says: the sky is blue

# >>> ae.lecture('the sky is blue')
# It is obvious that I believe that eric says: the sky is blue

# 6-3
class Professor(Lecturer):
    
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)
# >>> pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue 

# >>> ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue 
