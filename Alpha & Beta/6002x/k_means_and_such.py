import pylab


def minkowski_distance(v, w, p):
    """Assumes v and w are equal-length arrays of numbers.
    Returns Minkowski distance of order p between v and w"""
    distance = 0
    for i in range(len(v)):
        distance += abs(v[i] - w[i])**p
    return distance**(1 / p)


class Animal(object):

    def __init__(self, name, features):
        """Assumes name is string; featrues a list of numbers"""
        self.name = name
        self.features = pylab.array(features)

    def get_name(self):
        return self.name

    def get_features(self):
        return self.features

    def distance(self, other):
        """Assumes other is an Animal
        Returns the Euclidean distance between feature vectors
        of self and other"""
        return minkowski_distance(self.get_features(), other.get_features(), 2)


def compare_animals(animals, precision):
    """Assumes animals is a list of animals, precision is an int >= 0
        Builds a table of Euclidean distance between each animal"""
    column_labels = []
    for animal in animals:
        column_labels.append(animal.get_name())
    row_labels = column_labels[:]
    table_values = []
    for animal_row in animals:
        row = []
        for animal_column in animals:
            if animal_row == animal_column:
                row.append('--')
            else:
                distance = animal_row.distance(animal_column)
                row.append(str(round(distance, precision)))
        table_values.append(row)
    table = pylab.table(rowLabels=row_labels,
                        colLabels=column_labels,
                        cellText=table_values,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.2] * len(animals))
    table.scale(1, 2.5)
    pylab.savefig('distances')


class Example(object):

    def __init__(self, name, features, label=None):
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def get_features(self):
        return self.features[:]

    def get_label(self):
        return self.label

    def get_name(self):
        return self.name

    def distance(self, other):
        return minkowski_distance(self.get_features(), other.get_features(), 2)

    def __str__(self):
        return '{}: {}: {}'.format(self.get_name(), self.get_features(), self.get_label())


def main():
    # rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
    # boa = Animal('boa', [0, 1, 0, 1, 0])
    # dart_frog = Animal('dart frog', [1, 0, 1, 0, 4])
    # alligator = Animal('alligator', [1, 1, 0, 1, 4])
    # animals = [rattlesnake, boa, dart_frog, alligator]
    # compare_animals(animals, 3)

if __name__ == '__main__':
    main()
