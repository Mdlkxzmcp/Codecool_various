class Patient(object):

    def __init__(self, name, age, phone, code):
        self.name = name
        self.age = age
        self.phone = phone
        self.code = code

    def breath(self):
        print("I breath 12-18 times per minute")

    def walk(self, walkRate):
        print("I walk at {}km per hour".format(walkRate))


class CardioPatient(Patient):

    def __init__(self, name, age, phone, code, heartRate):
        super.__init__(self, name, age, phone, code)
        self.heartRate = heartRate

    def getHeartRate(self):
        print("My heart rate is: {}".format(self.heartRate))

    def setHeartRate(self, heartRate):
        self.heartRate = heartRate


class DiabetesPatient(Patient):

    def __init__(self, name, age, phone, code, bloodSugar):
        super.__init__(self, name, age, phone, code)
        self.bloodSugar = bloodSugar

    def getBloodSugar(self):
        print("My blood sugar is: {}".format(self.bloodSugar))

    def setBloodSugar(self, bloodSugar):
        self.bloodSugar = bloodSugar
