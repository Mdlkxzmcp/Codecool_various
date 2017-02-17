def Newton_Rapshon_method(num=2, epsilon=0.01):
    """
    Input: num, an int
           epsilon=0.01, the approximation margin
    Returns square root of num
    """

    guess = num / 2.0

    while abs(guess * guess - num) >= epsilon:
        numGuesses += 1
        guess -= ((guess ** 2) - num) / (2 * guess)
    return guess
