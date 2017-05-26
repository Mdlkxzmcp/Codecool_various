import random
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


class Location(object):

    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, delta_X, delta_Y):
        """delta_X and delta_Y are floats"""
        return Location(self.x + delta_X, self.y + delta_Y)

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def distance_from(self, other):
        x_distance = self.x - other.x
        y_distance = self.y - other.y
        return (x_distance**2 + y_distance**2)**0.5

    def __str__(self):
        return '<{},{}>'.format(self.x, self.y)


class Field(object):

    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, location):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = location

    def get_location(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_distance, y_distance = drunk.take_step()
        current_location = self.drunks[drunk]
        # use move method of Location to get new Location
        self.drunks[drunk] = current_location.move(x_distance, y_distance)


class OddField(Field):

    def __init__(self, number_of_wormholes=1000, x_range=100, y_range=100):
        super().__init__()
        self.wormholes = {}
        for wormhole in range(number_of_wormholes):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            new_x = random.randint(-x_range, x_range)
            new_y = random.randint(-y_range, y_range)
            new_location = Location(new_x, new_y)
            self.wormholes[(x, y)] = new_location

    def move_drunk(self, drunk):
        super().move_drunk(drunk)
        x = self.drunks[drunk].get_X()
        y = self.drunks[drunk].get_Y()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


class Drunk(object):

    def __init__(self, name='Bob'):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):

    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)


class ColdDrunk(Drunk):

    def take_step(self):
        step_choices = [(0, 0.9), (0, -1.03), (1.03, 0), (-1.03, 0)]
        return random.choice(step_choices)


class EDrunk(Drunk):

    def take_step(self):
        angle = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))


class PhotoDrunk(Drunk):

    def take_step(self):
        step_choices = [(0, 0.5), (0, 0.5), (1.5, 0), (-1.5, 0)]
        return random.choice(step_choices)


class DDrunk(Drunk):

    def take_step(self):
        step_choices = [(0.85, 0.85), (-0.85, -0.85), (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(step_choices)


def walk(field, drunk, number_of_steps):
    """Assumes: field a Field, drunk a Drunk in field,
        and number_of_steps an int >= 0.
        Moves drunk number_of_steps times;
    Returns the distance between the final location
        and the location at the start of the walk."""
    start = field.get_location(drunk)
    for step in range(number_of_steps):
        field.move_drunk(drunk)
    return start.distance_from(field.get_location(drunk))


def simulate_walks(number_of_steps, number_of_trials, drunk_class):
    """Assumes number_of_steps an int >= 0, number_of_trials an int > 0,
        drunk_class a subclass of Drunk.
    Simulates number_of_trials walks of number_of_steps steps each.
    Returns a list of the final distances for each trial"""
    Homer = drunk_class('Homer')
    origin = Location(0, 0)
    distances = []
    for trial in range(number_of_trials):
        field = Field()
        field.add_drunk(Homer, origin)
        distances.append(round(walk(field, Homer, number_of_steps), 1))

    return distances


def drunk_test(walk_lengths, number_of_trials, drunk_class):
    """Assumes walk_lengths a sequence of ints >= 0,
        number_of_trials an int > 0, and drunk_class a subclass of Drunk
    For each number of steps in walk_lengths, runs simulate_walks
        with number_of_trials walks and prints result"""
    for number_of_steps in walk_lengths:
        distances = simulate_walks(number_of_steps, number_of_trials, drunk_class)
        print('{} random walk of {} steps'.format(drunk_class.__name__, number_of_steps))
        print('Mean = {}'.format(round(sum(distances) / len(distances), 4)))
        print('Max = {}\nMin = {}'.format(max(distances), min(distances)))


class style_iterator(object):

    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def simulate_drunk(number_of_trials, drunk_class, walk_lengths):
    mean_distances = []
    for number_of_steps in walk_lengths:
        print('Starting simulation of ({} steps)'.format(number_of_steps))
        trials = simulate_walks(number_of_steps, number_of_trials, drunk_class)
        mean = sum(trials) / len(trials)
        mean_distances.append(mean)
    return mean_distances


def simulate_all(drunk_kinds, walk_lengths, number_of_trials):
    style_choice = style_iterator(('m-', 'b--', 'g-.'))
    for drunk_class in drunk_kinds:
        current_style = style_choice.next_style()
        print('Starting simulation of {}'.format(drunk_class.__name__))
        means = simulate_drunk(number_of_trials, drunk_class, walk_lengths)
        plt.plot(walk_lengths, means, current_style, label=drunk_class.__name__)
    plt.title('Mean Distance from Origin {} trials'.format(number_of_trials))
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc='best')


def get_final_locations(number_of_steps, number_of_trials, drunk_class):
    locations = []
    drunk = drunk_class()
    for trial in range(number_of_trials):
        field = Field()
        field.add_drunk(drunk, Location(0, 0))
        for step in range(number_of_steps):
            field.move_drunk(drunk)
        locations.append(field.get_location(drunk))
    return locations


def plot_locations(drunk_kinds, number_of_steps, number_of_trials):
    style_choice = style_iterator(('k+', 'r^', 'mo'))
    for drunk_class in drunk_kinds:
        locations = get_final_locations(number_of_steps, number_of_trials, drunk_class)
        x_values, y_values = [], []
        for location in locations:
            x_values.append(location.get_X())
            y_values.append(location.get_Y())
        x_values = pylab.array(x_values)
        y_values = pylab.array(y_values)
        mean_x = sum(abs(x_values)) / len(x_values)
        mean_y = sum(abs(y_values)) / len(y_values)
        current_style = style_choice.next_style()
        plt.plot(x_values, y_values, current_style,
                 label='{} mean absolute distance = <{},{}>'.format(drunk_class.__name__, mean_x, mean_y))
        pylab.title('Location at End of Walks ({} steps)'.format(number_of_steps))
        pylab.ylim(-1000, 1000)
        pylab.xlim(-1000, 1000)
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc='upper left')


def trace_walk(field_kinds, number_of_steps):
    style_choice = style_iterator(('b+', 'r^', 'ko'))
    for field_class in field_kinds:
        drunk = UsualDrunk()
        field = field_class()
        field.add_drunk(drunk, Location(0, 0))
        locations = []
        for step in range(number_of_steps):
            field.move_drunk(drunk)
            locations.append(field.get_location(drunk))
        x_values, y_values = [], []
        for location in locations:
            x_values.append(location.get_X())
            y_values.append(location.get_Y())
        current_style = style_choice.next_style()
        pylab.plot(x_values, y_values, current_style, label=field_class.__name__)
        pylab.title('Spots Visited on Walk ({} steps)'.format(number_of_steps))
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc='best')


def walkVector(field, drunk, number_of_steps):
    start = field.get_location(drunk)
    for step in range(number_of_steps):
        field.move_drunk(drunk)
    return(field.get_location(drunk).get_X() - start.get_X(),
           field.get_location(drunk).get_Y() - start.get_Y())


def main():

    # simulate_all((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)

    # random.seed(0)
    # plot_locations((UsualDrunk, ColdDrunk), 10000, 1000)

    # trace_walk((Field, OddField), 500)

if __name__ == "__main__":
    main()
