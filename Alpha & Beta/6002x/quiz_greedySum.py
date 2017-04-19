def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    current_sum = 0
    multipliers = []
    for index, num in enumerate(L):
        multiplier = 0
        if index == 0:
            while num * (multiplier + 1) <= s:
                multiplier += 1
            current_sum += num * multiplier
            multipliers.append(multiplier)
        elif index > 0:
            while (num * (multiplier + 1) + sum(L[i] * multipliers[i] for i in range(0, index))) <= s:
                multiplier += 1
            current_sum += num * multiplier
            multipliers.append(multiplier)
    if current_sum == s:
        return sum(multipliers)
    else:
        return "no solution"


assert greedySum([], 10) == 'no solution'
assert greedySum([16, 12, 5, 3, 1], 15) == 2
assert greedySum([15, 12, 4, 3, 1], 29) == 4
assert greedySum([10, 9, 8, 1], 17) == 8
assert greedySum([1], 20) == 20
print('win')
