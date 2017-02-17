def decimal_to_binary(num=2):
    """
    Input: num, an int
    Returns binary representation of num
    """

    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False
    result = ''
    if num == '0':
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    if is_neg:
        result = '-' + result
    return result
