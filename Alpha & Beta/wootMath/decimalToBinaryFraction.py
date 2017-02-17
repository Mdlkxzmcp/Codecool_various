def decimal_to_binary_fraction(x=0.5):
    """
    Input: x, a float between 0 and 1
    Returns binary representation of x
    """
    p = 0
    while ((2 ** p) * x) % 1 != 0:
        # print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
        p += 1

    num = int(x * (2 ** p))

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num //= 2

    for i in range(p - len(result)):
        result = '0' + result

    result = result[0:-p] + '.' + result[-p:]

    return result  # If there is no integer p such that x*(2**p) is a whole number, then internal
# representation is always an approximation

# Suggest that testing equality of floats is not exact: Use abs(x-y) < some
#   small number, rather than x == y

# Why does print(0.1) return 0.1, if not exact?
# Because Python designers set it up this way to automatically round
