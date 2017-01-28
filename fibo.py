def fibos(iteration):
    """funcion that prints fibonacci numbers up to a given number"""
    nr_of_iteration = 1
    num1 = 0
    num2 = 1
    while(iteration > 0):
        print(format(nr_of_iteration) + ": " + format(num1))
        num1, num2 = num2, num1 + num2
        iteration -= 1
        nr_of_iteration += 1

def fibo_efficient(num, dic={1:1, 2:2}):
    """
    Input: num of the fibonacci sequence to be returned
           dic={1:1, 2:2}, a dictionary with calculated values
    Returns answer, the value of given num in the fibonacci sequence
    """
    if num in dic:
        return dic[num]
    else:
        answer = fibo_efficient(num - 1, dic) + fibo_efficient(num - 2, dic)
        dic[num] answer
        return answer
