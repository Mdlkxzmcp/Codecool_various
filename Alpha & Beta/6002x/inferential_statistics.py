import scipy.integrate
import pylab
import random


class FairRoulette():

    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None
        self.black_odds, self.red_odds = 1, 1
        self.pockets_odds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def is_black(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28)):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1

    def is_red(self):
        return type(self.ball) == int and not self.is_black()

    def bet_black(self, ammount):
        if self.is_black():
            return ammount * self.black_odds
        else:
            return -ammount

    def bet_red(self, ammount):
        if self.is_red():
            return ammount * self.red_odds
        else:
            return -ammount

    def bet_pocket(self, pocket, ammount):
        if str(pocket) == str(self.ball):
            return ammount * self.pockets_odds
        else:
            return -ammount

    def __str__(self):
        return "Fair Roulette"


class EuropeanRoulette(FairRoulette):

    def __init__(self):
        super().__init__()
        self.pockets.append('0')

    def __str__(self):
        return "European Roulette"


class AmericanRoulette(EuropeanRoulette):

    def __init__(self):
        super().__init__()
        self.pockets.append('00')

    def __str__(self):
        return "American Roulette"


def playRoulette(game, number_of_spins, lucky_number='2', bet=1, to_print=True):
    total_red, total_black, total_pocket = 0, 0, 0
    for spin in range(number_of_spins):
        game.spin()
        total_red += game.bet_red(bet)
        total_black += game.bet_black(bet)
        total_pocket += game.bet_pocket(lucky_number, bet)
    if to_print:
        print(number_of_spins, 'spins of', game)
        print('Expected return betting red = {}%'.format(100 * total_red / number_of_spins))
        print('Expected return betting black = {}%'.format(100 * total_black / number_of_spins))
        print('Expected return betting "{}" = {}%\n'.format(lucky_number, 100 * total_pocket / number_of_spins))
    return (total_red / number_of_spins, total_black / number_of_spins, total_pocket / number_of_spins)


def findPocketReturn(game, number_of_trials, trial_size, to_print=False):
    pocket_returns = []
    for trial in range(number_of_trials):
        trial_values = playRoulette(game, trial_size, to_print=to_print)
        pocket_returns.append(trial_values[2])
    return pocket_returns


def getMeanAndStandardDeviation(samples):
    mean = sum(samples) / len(samples)
    total = 0
    for sample in samples:
        total += (sample - mean) ** 2
        standard_deviation = (total / len(samples)) ** 0.5
    return mean, standard_deviation


def simulateRoulettes(games, number_of_trials):
    result_dictionary = {}
    for game in games:
        result_dictionary[game().__str__()] = []
    for number_of_spins in (100, 1000, 10000, 100000):
        print('\nSimulate betting a pocket for {} trials of {} spins each'.format(number_of_trials, number_of_spins))
        for game in games:
            pocket_returns = findPocketReturn(game(), number_of_trials, number_of_spins, to_print=False)
            print('Expected return for {} = {:0.3f}%'.format(game(), 100 * sum(pocket_returns) / len(pocket_returns)))


def simulateRoulettesWithStandardDeviation(games, number_of_trials):
    result_dictionary = {}
    for game in games:
        result_dictionary[game().__str__()] = []
    for number_of_spins in (100, 1000, 10000, 100000):
        print('\nSimulate betting a pocket for {} trials of {} spins each'.format(number_of_trials, number_of_spins))
        for game in games:
            pocket_returns = findPocketReturn(game(), number_of_trials, number_of_spins, to_print=False)
            mean, standard_deviation = getMeanAndStandardDeviation(pocket_returns)
            result_dictionary[game().__str__()].append((number_of_spins, 100 * mean, 100 * standard_deviation))
            print('Expected return for {} = {:0.3f}% +/- {:0.3f}% with 95% confidence'.format(game(), 100 * mean, 100 * 1.96 * standard_deviation))


def gaussian(x, mu, sigma):
    factor_1 = 1 / (sigma * ((2 * pylab.pi) ** 0.5))
    factor_2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor_1 * factor_2


def checkEmpirical(number_of_trials):
    for trial in range(number_of_trials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('\nFor mu = {} and sigma = {}'.format(mu, sigma))
        for number_in_standard_deviation in (1, 1.96, 3):
            lower_limit_of_integration = mu - number_in_standard_deviation * sigma
            upper_limit_of_intergration = mu + number_in_standard_deviation * sigma
            area = scipy.integrate.quad(gaussian, lower_limit_of_integration, upper_limit_of_intergration, (mu, sigma))[0]
            print('Fraction within {} standard deviation = {:0.4f}'.format(number_in_standard_deviation, area))


def plotMeans(number_of_dice, number_of_rolls, number_of_bins, legend, color, style):
    means = []
    for i in range(number_of_rolls // number_of_dice):
        values = 0
        for dice in range(number_of_dice):
            values += 5 * random.random()
        means.append(values / number_of_dice)
    pylab.hist(means, number_of_bins, color=color, label=legend, weights=pylab.array(len(means) * [1]) / len(means), hatch=style)
    return getMeanAndStandardDeviation(means)


def main():
    # number_of_spins = 1000000
    # game = FairRoulette()
    # playRoulette(game, number_of_spins)
    #
    # random.seed(0)
    # number_of_trials = 20
    # games = (FairRoulette, EuropeanRoulette, AmericanRoulette)
    # simulateRoulettesWithStandardDeviation(games, number_of_trials)
    #
    # checkEmpirical(3)
    #
    # mean, standard_deviation = plotMeans(1, 1000000, 19, '1 die', 'b', '*')
    # print("Mean of rolling 1 die = {}, standard deviation = {}".format(mean, standard_deviation))
    # mean, standard_deviation = plotMeans(50, 1000000, 19, '50 dice', 'r', '//')
    # print("Mean of rolling 50 dice = {}, standard deviation = {}".format(mean, standard_deviation))
    # pylab.title('Rolling Continous Dice')
    # pylab.xlabel('Value')
    # pylab.ylabel('Probability')
    # pylab.legend()
    # pylab.show()
    #
    # number_of_trials = 50000
    # number_of_spins = 200
    # game = FairRoulette()
    # means = []
    # for trial in range(number_of_trials):
    #     means.append(findPocketReturn(game, 1, number_of_spins)[0] / number_of_spins)
    # pylab.hist(means, bins=19, weights=pylab.array(len(means) * [1]) / len(means))
    # pylab.xlabel('Mean Return')
    # pylab.ylabel('Probability')
    # pylab.title('Expected Return Betting a Pocket')
    # pylab.show()

if __name__ == '__main__':
    main()
