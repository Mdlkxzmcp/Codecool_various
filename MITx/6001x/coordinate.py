class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return (self.getX() == other.getX()) and (self.getY() == other.getY())

    def __repr__(self):
        return "Coordinate({},{})".format(self.getX(), self.getY())

coor1 = Coordinate(10, 20)
coor2 = Coordinate(10, 20)
print(coor1 == coor2)
print(eval(repr(coor1)) == coor2)
