import numpy as np


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    result = []

    def compare(numbers, total):
        if total == 0:
            return 1, []
        elif total < 0 or len(numbers) == 0:
            return 0, []

        if total > numbers[0]:
            take = compare(numbers[1:], total - numbers[0])
            leave = compare(numbers[1:], total)
            if take[0] == 1:
                take[1].append(numbers[0])
                return 1, take[1]
            if leave[0] == 1:
                return 1, leave[1]
            take[1].append(numbers[0])
            return 0, take[1]

        if total < numbers[0]:
            return compare(numbers[1:], total)

        return 1, [numbers[0]]

    chosen = compare(sorted(choices, reverse=True), total)[1]

    for number in choices:
        if number in chosen:
            chosen.pop(chosen.index(number))
            result.append(1)
        else:
            result.append(0)

    return np.asarray(result)

print(find_combination([3, 10, 2, 1, 5], 12), '== [0, 1, 1, 0, 0] ?')
print(find_combination([10, 10, 11, 11, 11], 20), '== [1, 1, 0, 0, 0] ?')
print(find_combination([1, 81, 3, 102, 450, 10], 9), '== [1, 0, 1, 0, 0, 0] ?')
print(find_combination([105, 10, 9, 6, 4], 120), '== [1, 0, 1, 1, 0] ?')
print('if all above are true then _win_')
