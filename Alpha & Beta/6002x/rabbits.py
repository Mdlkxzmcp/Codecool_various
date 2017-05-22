import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    new_rabbits = 0
    for rabbit in range(CURRENTRABBITPOP):
        if random.random() <= (1 - (CURRENTRABBITPOP / MAXRABBITPOP)):
            new_rabbits += 1
    CURRENTRABBITPOP += new_rabbits
    if CURRENTRABBITPOP > 1000:
        CURRENTRABBITPOP = 1000


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    new_foxes = 0
    foxes_that_died = 0
    for fox in range(CURRENTFOXPOP):
        if random.random() <= (CURRENTRABBITPOP / MAXRABBITPOP) and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= (1 / 3):
                new_foxes += 1
                continue
        elif random.random() <= 0.1 and CURRENTFOXPOP > 10:
            foxes_that_died += 1

    CURRENTFOXPOP += new_foxes
    CURRENTFOXPOP -= foxes_that_died


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    return rabbit_populations, fox_populations


def main():
    rabbit_populations, fox_populations = runSimulation(200)
    pylab.plot(rabbit_populations, fox_populations)
    pylab.xlabel('rabbit populations')
    pylab.ylabel('fox populations')
    pylab.show()

if __name__ == '__main__':
    main()
