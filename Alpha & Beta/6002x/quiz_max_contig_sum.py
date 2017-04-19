def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_contiguous_sum = 0
    point = 0
    for subsequence in range(len(L)):
        current_subsequence = []
        for index, number in enumerate(L[point:]):
            if not current_subsequence and number <= 0:
                continue
            else:
                try:
                    if sum(current_subsequence) + number > sum(current_subsequence) or sum(current_subsequence) + L[index + 1] > sum(current_subsequence) + number:
                        current_subsequence.append(number)
                        if sum(current_subsequence) > max_contiguous_sum:
                            max_contiguous_sum = sum(current_subsequence)
                    else:
                        current_subsequence = []
                except IndexError:
                    if sum(current_subsequence) + number > sum(current_subsequence):
                        current_subsequence.append(number)
                        if sum(current_subsequence) > max_contiguous_sum:
                            max_contiguous_sum = sum(current_subsequence)
        point += 1
    return max_contiguous_sum

assert max_contig_sum([1]) == 1
assert max_contig_sum([1, -1]) == 1
assert max_contig_sum([10, 9, 8, -1]) == 27
assert max_contig_sum([0, -2, -5, -1, 5]) == 5
assert max_contig_sum([3, 4, -1, 5, -4]) == 11
assert max_contig_sum([3, 4, -8, 15, -1, 2]) == 16
assert max_contig_sum([3, 4, -8, 3, 3, 1, -7, 15, -1, 2]) == 16
assert max_contig_sum([0, -2, -7, 3, 3, -7, 15, 2]) == 17
print('win')
