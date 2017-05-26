class fraction (object):

    def __init__(self, numerator, denominator):
        self. numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return("{}/{}".format(self.numerator, self.denominator))

    def getNumer(self):
        return self.numerator

    def getDenom(self):
        return self.denominator

    def __add__(self, other):
        numerator = self.getNumer() * other.getDenom() + self.getDenom() * other.getNumer()
        denominator = self.getDenom() * other.getDenom()
        return fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.getNumer() * other.getDenom() - self.getDenom() * other.getNumer()
        denominator = self.getDenom() * other.getDenom()
        return fraction(numerator, denominator)

    def convert(self):
        """Returns a float value of the fraction"""
        return self.getNumer() / self.getDenom()
