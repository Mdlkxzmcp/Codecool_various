class Treasure(object):

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def value_to_weight(self):
        return self.getValue() / self.getWeight()

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


def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
        keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxCost:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('  ', item)


def testGreedys(treasures, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'weights')
    testGreedy(treasures, maxUnits, Treasure.getValue)
    print('\nUse greedy by weight to allocate', maxUnits, 'weights')
    testGreedy(treasures, maxUnits, lambda x: 1 / Treasure.getWeight(x))
    print('\nUse greedy by ratio to allocate', maxUnits, 'weights')
    testGreedy(treasures, maxUnits, Treasure.value_to_weight)


def maxVal(toConcider, availableWeight):
    """Assumes toConcider a list of items,
            availableWeight a weight
        Returns a tuple of the total value of a
        solution to 0/1 knapsack problem and
        the items of that solution"""
    if toConcider == [] or availableWeight == 0:
        result = (0, ())
    elif toConcider[0].getWeight() > availableWeight:
        result = maxVal(toConcider[1:], availableWeight)
    else:
        nextItem = toConcider[0]
        withValue, withToTake = maxVal(toConcider[1:], availableWeight - nextItem.getWeight())
        withValue += nextItem.getValue()
        withoutValue, withoutToTake = maxVal(toConcider[1:], availableWeight)
        if withValue > withoutValue:
            result = (withValue, withToTake + (nextItem,))
        else:
            result = (withoutValue, withoutToTake)
    return result


def testMaxVal(treasures, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits, 'weights')
    value, taken = maxVal(treasures, maxUnits)
    print('Total value of items taken =', value)
    if printItems:
        for item in taken:
            print('   ', item)


names = ['gold', 'bow', 'skull', 'book', 'scarab', 'arrow', 'tom', 'scroll', 'mask']
values = [89, 90, 95, 100, 90, 79, 50, 10]
weights = [123, 154, 258, 354, 365, 150, 95, 195]
treasures = buildTemple(names, values, weights)
testGreedys(treasures, 750)
print('\n\n')
testMaxVal(treasures, 750)
