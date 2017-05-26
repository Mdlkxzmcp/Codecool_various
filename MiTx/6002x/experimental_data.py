import pylab
import numpy as np
import random


def get_data(file_name):
    data_file = open(file_name, 'r')
    distances = []
    masses = []
    discard_header = data_file.readline()
    for line in data_file:
        distance, mass = line.split()
        distances.append(distance)
        masses.append(mass)
    data_file.close()
    return (masses, distances)


def label_plot():
    pylab.title('Measured Displacement of the spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')


def plot_data(file_name):
    x_values, y_values = get_data(file_name)
    x_values = pylab.array(x_values)
    y_values = pylab.array(y_values)
    x_values = x_values * 9.81  # g on Earth
    pylab.plot(x_values, y_values, 'bo', label='Measured displacements')
    label_plot()


def test_errors(number_of_trials=10000, number_of_points=100):
    results = [0] * number_of_trials
    for trial in range(number_of_trials):
        sum_of_random_points = 0
        for point in range(number_of_points):
            sum_of_random_points += random.triangular(-1, 1)
        results[trial] = sum_of_random_points
    # plot results in a histogram
    pylab.hist(results, bins=50)
    pylab.title('Sum of 100 random points -- Triangular PDF (10,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')


def fit_data_1(file_name):
    x_values, y_values = get_data(file_name)
    x_values = pylab.array(x_values)
    y_values = pylab.array(y_values)
    x_values = x_values * 9.81  # convert mass to force (F = mg)
    pylab.plot(x_values, y_values, 'ro', label='Measured points')
    label_plot()
    a, b = pylab.polyfit(x_values, y_values, 1)  # fit y = ax + b
    estimated_values = a * x_values + b
    pylab.plot(x_values, estimated_values, 'r', label='Linear fit. k = {:0.5f}'.format(1 / a))
    pylab.legend(loc='best')


def fit_data_2(file_name):
    x_values, y_values = get_data(file_name)
    x_values = pylab.array(x_values)
    y_values = pylab.array(y_values)
    x_values = x_values * 9.81  # convert mass to force (F = mg)
    pylab.plot(x_values, y_values, 'ro', label='Measured displacements')
    label_plot()
    model = pylab.polyfit(x_values, y_values, 1)
    estimated_values = pylab.polyval(model, x_values)
    pylab.plot(x_values, estimated_values, 'r', label='Linear fit. k = {:0.5f}'.format(1 / model[0]))
    a, b, c, d = pylab.polyfit(x_values, y_values, 3)
    estimated_values = a * (x_values**3) + b * x_values**2 + c * x_values + d
    pylab.plot(x_values, estimated_values, label='Cubic fit')
    pylab.legend(loc='best')


def fit_data_3(file_name):
    x_values, y_values = get_data(file_name)
    extra_x = pylab.array(x_values + [1.05, 1.1, 1.15, 1.2, 1.25])
    x_values = pylab.array(x_values)
    y_values = pylab.array(y_values)
    x_values = x_values * 9.81  # convert mass to force (F = mg)
    extra_x = extra_x * 9.81
    pylab.plot(x_values, y_values, 'bo', label='Measured displacements')
    label_plot()
    a, b = pylab.polyfit(x_values, y_values, 1)
    estimated_values = a * extra_x + b
    pylab.plot(extra_x, estimated_values, label='Linear fit')
    a, b, c, d = pylab.polyfit(x_values, y_values, 3)
    estimated_values = a * (extra_x**3) + b * extra_x**2 + c * extra_x + d
    pylab.plot(extra_x, estimated_values, label='Cubic fit')
    pylab.legend(loc='best')


def fit_data_4(file_name):
    x_values, y_values = get_data(file_name)
    x_values = pylab.array(x_values[:-6])
    y_values = pylab.array(y_values[:-6])
    x_values = x_values * 9.81  # convert mass to force (F = mg)
    pylab.plot(x_values, y_values, 'bo', label='Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(x_values, y_values, 1)  # fix y = ax + b
    # use line equation to graph predicted values
    estimated_values = a * x_values + b
    k = 1 / a
    pylab.plot(x_values, estimated_values, label='Linear fit, k = {:0.5f}'.format(k))
    pylab.legend(loc='best')


def get_trajectory_data(file_name):
    data_file = open(file_name, 'r')
    distances = []
    heights1, heights2, heights3, heights4 = [], [], [], []
    discard_header = data_file.readline()
    for line in data_file:
        distance, h1, h2, h3, h4 = line.split()
        distances.append(distance)
        heights1.append(h1)
        heights2.append(h2)
        heights3.append(h3)
        heights4.append(h4)
    data_file.close()
    return (distances, [heights1, heights2, heights3, heights4])


def average_mean_square_error(data, predicted):
    error = 0
    for i in range(len(data)):
        error += (data[i] - predicted[i])**2
    return error / len(data)


def r_squared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    mean_error = error / len(predicted)
    return 1 - (mean_error / np.var(observed))


def generate_fits(x_values, y_values, degrees):
    return [pylab.polyfit(x_values, y_values, degree) for degree in degrees]


def test_fits(models, degrees, x_values, y_values, title):
    pylab.plot(x_values, y_values, 'o', label='Data')
    for index, model in enumerate(models):
        estimated_values = pylab.polyval(model, x_values)
        error = r_squared(y_values, estimated_values)
        pylab.plot(x_values, estimated_values, label='Fit of degree {}, R^2 = {:0.5f}'.format(degrees[index], error))
        pylab.legend(loc='best')
        pylab.title(title)


def try_fits_1(file_name):
    distances, heights = get_trajectory_data(file_name)
    distances = pylab.array(distances) * 36
    total_heights = pylab.array([0] * len(distances))
    for height in heights:
        total_heights = total_heights + pylab.array(height)
    pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    mean_heights = total_heights / len(heights)
    pylab.plot(distances, mean_heights, 'bo')
    a, b = pylab.polyfit(distances, mean_heights, 1)
    altitudes = a * distances + b
    pylab.plot(distances, altitudes, 'r', label='Linear Fit')
    a, b, c = pylab.polyfit(distances, mean_heights, 2)
    altitudes = a * (distances**2) + b * distances + c
    pylab.plot(distances, altitudes, 'g', label='Quadratic Fit')
    pylab.legend()


def try_fits_2(file_name):
    distances, heights = get_trajectory_data(file_name)
    distances = pylab.array(distances) * 36
    total_heights = pylab.array([0] * len(distances))
    for h in heights:
        total_heights = total_heights + pylab.array(h)
    pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    mean_heights = total_heights / len(heights)
    pylab.plot(distances, mean_heights, 'bo')
    a, b = pylab.polyfit(distances, mean_heights, 1)
    altitudes = a * distances + b
    pylab.plot(distances, altitudes, 'r', label='Linear Fit, R2 = {:0.4f}'.format(r_square(mean_heights, altitudes)))
    a, b, c = pylab.polyfit(distances, mean_heights, 2)
    altitudes = a * (distances**2) + b * distances + c
    pylab.plot(distances, altitudes, 'g', label='Quadratic Fit, R2 = {:0.4f}'.format(r_square(mean_heights, altitudes)))
    pylab.legend()


def r_square(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    SEE = ((estimated - measured)**2).sum()
    mMean = measured.sum() / float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - SEE / MV


def generate_noisy_parabolic_data(a, b, c, x_values, file_name):
    y_values = []
    for x in x_values:
        theoretical_value = a * x**2 + b * x + c
        y_values.append(theoretical_value + random.gauss(0, 35))
    save_file = open(file_name, 'w')
    save_file.write('x      y\n')
    for index, value in enumerate(y_values):
        save_file.write('{}     {}\n'.format(value, x_values[index]))
    save_file.close()


def train_test_and_report(x_values, y_values, number_of_subsets, dimensions):

    def split_data(x_values, y_values):
        to_train = random.sample(range(len(x_values)), len(x_values) // 2)
        train_x, train_y, test_x, test_y = [], [], [], []
        for indice in range(len(x_values)):
            if indice in to_train:
                train_x.append(x_values[indice])
                train_y.append(y_values[indice])
            else:
                test_x.append(x_values[indice])
                test_y.append(y_values[indice])
        return train_x, train_y, test_x, test_y

    r_squares = {}
    for dimension in dimensions:
        r_squares[dimension] = []

    for subset in range(number_of_subsets):
        train_x, train_y, test_x, test_y = split_data(x_values, y_values)
        for dimension in dimensions:
            model = pylab.polyfit(train_x, train_y, dimension)
            estimated_values = pylab.polyval(model, test_x)
            r_squares[dimension].append(r_squared(test_x, estimated_values))

    print('Mean R-squares for test data')
    for dimension in dimensions:
        mean = sum(r_squares)
        standard_deviation = np.std(r_squares[dimension])
        print('For dimensionality {}: mean = {:0.4f}, standard deviation = {:0.4f}'.format(mean, standard_deviation))


def main():
    # parameters for generating data
    # x_values = range(-10, 11, 1)
    # a, b, c = 3, 0, 0
    # generate_noisy_parabolic_data(a, b, c, x_values, 'Mystery_Data.txt')
    #
    # degrees = (2, 4, 8, 16)
    #
    # x_values_1, y_values_1 = get_data('Dataset_1.txt')
    # models_1 = generate_fits(x_values_1, y_values_1, degrees)
    # test_fits(models_1, degrees, x_values_1, y_values_1, 'DataSet 1.txt')
    #
    # pylab.figure()
    # x_values_2, y_values_2 = get_data('Dataset_2.txt')
    # models_2 = generate_fits(x_values_2, y_values_2, degrees)
    # test_fits(models_2, degrees, x_values_2, y_values_2, 'DataSet 2.txt')
    #
    # pylab.figure()
    # test_fits(models_1, degrees, x_values_2, y_values_2, 'DataSet 2/Model 1')
    # pylab.figure()
    # test_fits(models_2, degrees, x_values_1, y_values_1, 'DataSet 1/Model 2')
    #
    # number_of_subsets = 10
    # dimensions = (1, 2, 3)
    # train_test_and_report(x_values, y_values, number_of_subsets, dimensions)

if __name__ == '__main__':
    main()
