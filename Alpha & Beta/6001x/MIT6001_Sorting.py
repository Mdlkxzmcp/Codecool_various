import random


def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)


def bubble_sort(L):  # O(n^2) where n is len(L)
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp


def selection_sort(L):  # O(n^2) -\\-
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1


def merge(left, right):  # O(n) -\\-
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):  # uses merge(l, r); O(log(n)) but with merge it's O(n*log(n)) -\\-
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
