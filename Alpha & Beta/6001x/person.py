import datetime


class Person(object):

    def __init__(self, name):
        """create a person called <name>"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
        less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name


class MITPerson(Person):

    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        # sorting MIT people uses their ID numbers, not names.
        return self.idNum < other.idNum

    def speak(self, utterance):
        return "{} says: '{}'".format(self.getLastName(), utterance)


class Professor(MITPerson):

    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        saying = "In course {} we say ".format(self.department)
        return MITPerson.speak(self, saying + utterance)

    def lecture(self, topic):
        return self.speak("it is obvious that {}".format(topic))


class Student(MITPerson):
    pass


class UG(Student):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for student in self.students:
            yield student


def gradeReport(course):
    """Assumes: course is of type Grades"""
    report = []
    for student in course.allStudents():
        total = 0.0
        numOfGrades = 0
        for grade in course.getGrades(student):
            total += grade
            numOfGrades += 1
        try:
            average = total / numOfGrades
            report.append("{}'s mean grade is {}".format(student, average))
        except ZeroDivisionError:
            report.append("{} has no grades".format(student))
    return '\n'.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Phil Collins', 2017)
ug4 = UG('Uncle Bob', 2019)
g1 = Grad('Bill Gates')
g2 = Grad('Steven Wilson')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g1, 90)
six00.addGrade(g2, 25)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 95)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 85)
six00.addGrade(ug2, 75)
six00.addGrade(ug3, 75)

print(gradeReport(six00))
