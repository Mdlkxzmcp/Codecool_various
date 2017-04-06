def naive(a, b):
    c = 0
    while a > 0:
        c = c + b
        a = a - 1
    return c


def russian(a, b):
    """
    The Russian Peasant Algorithm:
    Multiply one integer by the other integer.
    Input:    a, b: integers
    Returns:  a*b
    """
    c = 0
    while a > 0:
        if a % 2 == 1:
            c = c + b
        b = b << 1
        a = a >> 1
    return c


def rec_russian(a, b):
    if a == 0:
        return 0
    elif a % 2 == 0:
        return 2 * rec_russian(a / 2, b)
    else:
        return b + 2 * rec_russian((a - 1) / 2, b)
