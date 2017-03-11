# # # # # # # # # # # # # #
"""Complexity of O( log(n) )"""


def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result


def h(n):
    """ assume n is an int >= 0 """
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer


def bisection_search_2(L, e):  # assumes the list is sorted!
    def bisection_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisection_search_helper(L, e, low, mid - 1)
        else:
            return bisection_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisection_search_helper(L, e, 0, len(L) - 1)


# # # # # # # # # # # # # #
"""Complexity of O( n )"""


def addDigits(s):
    value = 0
    for char in s:
        value += int(char)
    return value


def fact_iter(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def linear_search(L, e):  # on a list
    for i in range(len(L)):
        if e == L[i]:
            return True
    return False


def search(L, e):  # on a sorted list
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


# # # # # # # # # # # # # #
"""Complexity of O( n*log(n) )"""


def bisection_search_1(L, e):  # assumes the list is sorted!
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisection_search_1(L[:half], e)  # adds complexity
        else:
            return bisection_search_1(L[half:], e)


# # # # # # # # # # # # # #
"""Complexity of O( n^2 )"""


def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1, L2):
    temp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                temp.append(e1)
    result = []
    for e in temp:
        if not (e in result):
            result.append(e)
    return result


# # # # # # # # # # # # # #
"""Complexity of O( 2^n )"""


def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        new.append(small + extra)  # for all smaller solutions, add one with last element
    return smaller + new  # combine those with last element and those without


def fib_recur(n):
    """ assumes n is an int >= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)

# # # # # # # # # # # # # #
