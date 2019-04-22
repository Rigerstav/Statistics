def linear_fit(x_points, y_points, dy_points):
    import matplotlib.pyplot as plt
    import numpy as np
    # this function create linear fit to data
    # it accept list of x measures, y measures and dy measures as input
    # it returns the best fitting a and b arguments
    # it also returns chi2 reduced
    # and plots the linear fit and residuals graph

    x_avg = find_avg(x_points)
    y_avg = find_avg(y_points)
    a = find_a(x_points, y_points, x_avg)
    b = find_b(a, x_avg, y_avg)
    print('a = {0}, b = {1}'.format(a, b))
    chi2_red = find_chi2_red(y_points, x_points, dy_points, a, b)
    print('chi2_red = {0}'.format(chi2_red))
    plot_linear(a, b, x_points, y_points, dy_points)
    plot_residuals(x_points, y_points, dy_points, a, b)


def find_avg(data_points):  # this function calculates avg
    n = len(data_points)
    average = 0
    for i in data_points:
        average += i
    average = average/n
    return average


def find_a(x, y, x_avg):  # this function calculates the best a
    numerator = 0
    denominator = 0
    for i in x:
        numerator += (x[i]-x_avg)*y[i]
        denominator += ((x[i]-x_avg)**2)
    a = numerator/denominator
    return a


def find_b(a, x_avg, y_avg):  # this function calculates the best b
    b = y_avg-a*x_avg
    return b


def find_chi2_red(y, x, dy, a, b):  # this function calculates chi2 reduced
    chi2 = 0
    for i in x:
        chi2 += (y[i] - a*x[i] - b)/((dy[i])**2)
    ni = len(x)-2
    chi2_red = chi2/ni
    return chi2_red


def plot_linear(a, b, x, y, dy):
    import matplotlib.pyplot as plt
    import numpy as np
    min_x = min(x)
    max_x = max(x)
    t = np.arange(min_x, max_x + 0.2, 0.2)  # here we create points for the linear fit
    fit_line = a * t + b
    plt.plot(t, fit_line, 'r')
    plt.errorbar(x, y, xerr=None, yerr=dy, fmt='b+')
    return plt.show()


def plot_residuals(x, y, dy, a, b):
    import matplotlib.pyplot as plt
    fit_points = []
    for i in x:
        f_point = a*x[i] + b
        fit_points.append(f_point)
    residuals = []
    for i in range(0, len(y)):
        residuals.append(y[i] - fit_points[i])
    plt.plot(x, residuals, '.r')
    plt.errorbar(x, residuals, yerr=dy, xerr=None, fmt='b+')
    return plt.show()


linear_fit([0, 1, 2, 3, 4, 5], [0.92, 4.15, 9.78, 14.46, 17.26, 21.90], [0.5, 1.0, 0.75, 1.25, 1.0, 1.5])
