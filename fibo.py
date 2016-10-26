def fibo(number):
    "function that prints out the given fibonacci number"
    if number == 0 or number == 1:
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)

while True:
    try:
        number = int(
            input("Which fibo number do you need man? "))
        print(fibo(number))
    except ValueError:
        print("Woah there calm down, numbers please!")
        continue
    else:
        break
