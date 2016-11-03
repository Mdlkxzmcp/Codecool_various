def fibo(number):
    """function that prints out the given fibonacci number"""
    if number == 0 or number == 1:
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)


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

while True:
    try:
        choice = str(input(r"Do you want fibo 'number' or 'numbers' man? "))
    except TypeError:
        print(r"Hey 'number' or 'numbers' mannnnn")
        continue
    else:
        if choice == "numbers":
            try:
                iteration = int(
                    input("How many fibo numbers do ya need ma man? "))
            except ValueError:
                print("Woah there calm down, numbers please!")
                continue
            else:
                fibos(iteration)
        elif choice == "number":
            try:
                number = int(
                    input("Which fibo number do you need man? "))
                print(fibo(number))
            except ValueError:
                print("Woah woah dude man use numbers")
                continue
        else:
            print(r"Told you, 'number' or 'numbers' :|")
            break
