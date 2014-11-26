__author__ = 'Erik Nylander'

import numpy as np
from scipy.optimize import curve_fit
import Tkinter
import tkFileDialog
import timeit


def file_open():
    """
    Opens a file using the TKinter interface to open a file. The file needs to have the structure x, y, ...
    :return: a list of of x,y tuples
    """
    root = Tkinter.Tk()
    root.withdraw()
    f = tkFileDialog.askopenfile(mode='r')
    try:
        xy_lst = []
        for line in f:
            line = line.strip()
            line = line.split(',')
            try:
                point = (float(line[0]), float(line[1]))
                xy_lst.append(point)
            except ValueError:
                continue
        return xy_lst
    except TypeError:
        print 'No file was selected, exiting.'
        quit()


def lsr(points):
    """
    Calculates the ordinary least squares regression model for a data set.
    :param points: A list of tuples represent the points to be modeled.
    :return: The slope and y-intercept for the olsr model as a tuple.
    """
    x_sum = 0
    y_sum = 0
    xy_sum = 0
    xsquare_sum = 0
    n = len(points)
    for point in points:
        x_sum += point[0]
        y_sum += point[1]
        xy_sum += point[0]*point[1]
        xsquare_sum += point[0]**2
    slope_num = n * xy_sum - x_sum * y_sum
    slope_den = n * xsquare_sum - x_sum ** 2
    slope = slope_num/slope_den
    y_int = (y_sum - slope * x_sum)/n
    return slope, y_int

def funclin(x, a, b):
    return a * x + b


def linear(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funclin, x, y)
    return popt


def funcquad(x, a, b, c):
    return a * x**2 + b * x + c


def quad(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funcquad, x, y)
    return popt


def funcexp(t, a, b, c):
    return a*np.exp(-b*t) + c


def exp(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funcexp, x, y)
    return popt


def funcgauss(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))


def gauss(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funcgauss, x, y)
    return popt


def time(func, lst, n=10000):
    '''
    Prints the timing generated from the timeit function for the sort functions.
    :param func: function to be tested as a string
    :param lst: variable name for the list of values to be sorted as a string
    :param n: number of iterations of the timing function, defaults to 1,000,000
    :return: none
    '''

    t = timeit.timeit("%s(%s)" % (func, lst), setup="from __main__ import %s, %s" % (func, lst), number=n)
    print "Timing: %d loops in %f seconds" %(n, t)


if __name__ == '__main__':
    data = file_open()
    lsrreg = lsr(data)
    print 'Least Squares Regression Equation:'
    print 'Slope: %f, Y-intercept: %f' % (lsrreg[0], lsrreg[1])
    time('lsr', 'data')
    print ''

    scilin = linear(data)
    print 'SciPy Linear Regression Equation:'
    print 'Slope: %f, Y-intercept: %f' % (scilin[0], scilin[1])
    time('linear', 'data')
    print ''

    sciquad = quad(data)
    print 'SciPy Quadratic Regression Equation (ax^2 + bx + c):'
    print 'a: %f, b: %f, c: %f' % (sciquad[0], sciquad[1], sciquad[2])
    time('quad', 'data')
    print ''

    sciexp = exp(data)
    print 'SciPy Exponential Regression Equation (a * (-b^t) + c):'
    print 'a: %f, b: %f, c: %f' % (sciexp[0], sciexp[1], sciexp[2])
    time('exp', 'data')
    print ''

    scigauss = gauss(data)
    print 'SciPy Gaussian Regression Equation (a * exp((-(x-b)^2)/(2*c^2)):'
    print 'a: %f, b: %f, c: %f' % (scigauss[0], scigauss[1], scigauss[2])
    time('gauss', 'data')
    print ''