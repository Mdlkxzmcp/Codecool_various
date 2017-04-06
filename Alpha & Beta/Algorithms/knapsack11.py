class Treasure(object):

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def value_to_weight(self):
        return self.get_value() / self.get_weight()

    def __str__(self):
        return '{}: <{}, {}>'.format(self.name, self.value, self.weight)


def buildTemple(names, values, weights):
    """names, values, weights lists of same length.
    name a list of strings
    values and weights lists of numbers
    returns lists of Treasures"""
    temple = []
    for index in range(len(values)):
        temple.append(Treasure(names[index], values[index], weights[index]))
    return temple


def greedy(items, max_cost, key_function):
    """Assumes items a list, max_cost >= 0,
        key_function maps elements of items to numbers"""
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0.0, 0.0

    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight()) <= max_cost:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()

    return (result, total_value)


def testGreedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print('Total value of items taken =', val)
    for item in taken:
        print('  ', item)


def testGreedys(treasures, max_units):
    print('Use greedy by value to allocate', max_units, 'weights')
    testGreedy(treasures, max_units, Treasure.get_value)
    print('\nUse greedy by weight to allocate', max_units, 'weights')
    testGreedy(treasures, max_units, lambda x: 1 / Treasure.get_weight(x))
    print('\nUse greedy by ratio to allocate', max_units, 'weights')
    testGreedy(treasures, max_units, Treasure.value_to_weight)


def maxVal(to_consider, available_weight):
    """Assumes to_consider a list of items,
            available_weight a weight
        Returns a tuple of the total value of a
        solution to 0/1 knapsack problem and
        the items of that solution"""
    if to_consider == [] or available_weight == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > available_weight:
        result = maxVal(to_consider[1:], available_weight)
    else:
        next_item = to_consider[0]
        with_value, with_to_take = maxVal(to_consider[1:], available_weight - next_item.get_weight())
        with_value += next_item.get_value()
        without_value, without_to_take = maxVal(to_consider[1:], available_weight)
        if with_value > without_value:
            result = (with_value, with_to_take + (next_item,))
        else:
            result = (without_value, without_to_take)
    return result


def fastMaxVal(to_consider, available_weight, memo={}):
    """Assumes to_consider a list of items,
            available_weight a weight
            memo supplied by recursive calls
        Returns a tuple of the total value of a
        solution to 0/1 knapsack problem and
        the items of that solution"""
    if (len(to_consider), available_weight) in memo:
        result = memo[(len(to_consider), available_weight)]
    elif to_consider == [] or available_weight == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > available_weight:
        result = fastMaxVal(to_consider[1:], available_weight, memo)
    else:
        next_item = to_consider[0]
        # Explore left branch
        with_value, with_to_take = fastMaxVal(to_consider[1:], available_weight - next_item.get_weight(), memo)
        with_value += next_item.get_value()
        # Explore right branch
        without_value, without_to_take = fastMaxVal(to_consider[1:], available_weight, memo)
        # Choose better branch
        if with_value > without_value:
            result = (with_value, with_to_take + (next_item,))
        else:
            result = (without_value, without_to_take)
    memo[(len(to_consider), available_weight)] = result
    return result


def testMaxVal(treasures, max_units, algorithm, print_items=True):
    print('Using the {} algorithm.'.format(algorithm.__name__))
    print('Temple contains {} treasures'.format(len(treasures)))
    print('Use search tree to allocate', max_units, 'weights')
    value, taken = algorithm(treasures, max_units)
    print('Total value of items taken =', value)
    if print_items:
        for item in taken:
            print('   ', item)


names = ['gold', 'bow', 'skull', 'book', 'scarab', 'arrow', 'tom', 'scroll', 'mask']
values = [89, 90, 95, 100, 90, 79, 50, 10]
weights = [123, 154, 258, 354, 365, 150, 95, 195]
treasures = buildTemple(names, values, weights)
testGreedys(treasures, 750)
print('\n\n')
testMaxVal(treasures, 750, maxVal)
print('\n\n')
testMaxVal(treasures, 750, fastMaxVal)
