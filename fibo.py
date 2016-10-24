import sys


nr_of_iteration = 1
num1 = 0
num2 = 1

while True:
    try:
        iteration = int(
            input("How many fibbo numbers do ya need ma man? "))
    except ValueError:
        print("Woah there calm down, numbers please!")
        continue
    else:
        break

while(iteration > 0):
    print(format(nr_of_iteration) + ": " + format(num1))
    num1, num2 = num2, num1 + num2
    iteration -= 1
    nr_of_iteration += 1
