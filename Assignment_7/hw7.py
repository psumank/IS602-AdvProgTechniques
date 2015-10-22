__author__ = 'Suman'

import numpy as np
from scipy.optimize import curve_fit
import Tkinter
import tkFileDialog
import csv
import timeit


def read_datapoints():
    '''
      Read the data for regression analysis from a file [prompts for file]
      Return a list of tuples - A tuple here is a (x,y) co-ordinate.
         - x indicates the exploratory/independent variable.
         - y indicates the response/dependent variable.
    '''
    #Select and open the file in read mode & read the datastream
    root = Tkinter.Tk()
    root.withdraw()
    filename = tkFileDialog.askopenfilename(parent=root)
    dataStream = open(filename, 'r')

    #wrap into a csv data reader
    csvReader = csv.reader(dataStream)

    #Loop thru the rows and prepare a list of point tuples
    dataPoints = []
    for row in csvReader:
        if csvReader.line_num > 1: #ignore header line
            dataPoints.append( (float(row[1]), float(row[2])) )

    #Return the list of tuples
    return dataPoints

    
def calc_lsr(dataPoints):
    '''
    For a given data points, this calculates the least sqaures linear regression model.
    :parm dataPoints - A list of co-ordinate points that need to be modeled
    :returns - A tuple of b0 and b1. [bo] is the y-intercept and the [b1] is slope.
    '''

    #Initialize the variables, needed to calc the b0 and b1.
    x_Sum = 0;
    y_Sum = 0;
    xy_Sum = 0;
    xsquare_Sum = 0;
    n = len(dataPoints)

    #loop thru the dataPoints and figure out the above variables.
    for point in dataPoints:
        x_Sum += point[0]
        y_Sum += point[1]
        xy_Sum += point[0] * point[1]
        xsquare_Sum += point[0] ** 2

    #lets find out the b0 and b1 now.
    b1 = (n * xy_Sum - x_Sum * y_Sum) / (n * xsquare_Sum - x_Sum ** 2)
    b0 = (y_Sum - b1 * x_Sum)/n
    return b0, b1
    
def funcLine(x, a, b):
    """
    equation of line
    """
    return a * x + b


def scipy_calc_linear(dataPoints):
    """Calls the SciPy curve_fit function using a linear function funcLine we defined above"""
    x = []
    y = []
    for point in dataPoints:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funcLine, x, y)
    return popt
    
    
def funcQuadratic(x, a, b, c):
    return a * x**2 + b * x + c


def scipy_calc_quad(dataPoints):
    """Calls the SciPy curve_fit function using a quad function form - funcQuadratic - we defined above"""
    x = []
    y = []
    for point in dataPoints:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funcQuadratic, x, y)
    return popt


def funcGaussian(x, a, b, c):
    return a * np.exp(-(x-b)**2/(2*c**2))


def scipy_calc_gaussian(dataPoints):
    """Calls the SciPy curve_fit function using a Gaussian function form - funcGaussian - we defined above"""
    x = []
    y = []
    for point in dataPoints:
        x.append(point[0])
        y.append(point[1])
    popt, pcov = curve_fit(funcGaussian, x, y)
    return popt


def profile(func, lst, n=10000):
    '''
    Prints the timing generated from the timeit function for the given function.
    :Inputs:
    :func: function to be tested as a string
    :lst: variable name for the list of data points for curve_fit
    : n: number of iterations of the timing function, defaults to 10000
    :return: none
    '''
    t = timeit.timeit("%s(%s)" % (func, lst), setup="from __main__ import %s, %s" % (func, lst), number=n)
    print "Timing: %d iterations in %f seconds" %(n, t)
    

if __name__ == "__main__":
    data = read_datapoints()
    model = calc_lsr(data)
    print 'Regression Equation is ==>'
    print 'y-hat = %f + %f * x' % (model[0], model[1])
    print 'Here, b0 [Y-intercept] : %f,  b1 [Slope]: %f' % (model[0], model[1])
    profile('calc_lsr', 'data')
    print('---------------------------')

    scipyLR =  scipy_calc_linear(data)
    print 'SciPy Linear Regression Equation ==> '
    print 'y-hat = %f + %f * x' % (scipyLR[1], scipyLR[0])
    print 'Slope: %f, Y-intercept: %f' % (scipyLR[0], scipyLR[1])
    profile('scipy_calc_linear', 'data')
    print('---------------------------')

    scipyQuad = scipy_calc_quad(data)
    print 'SciPy Quadratic Regression Equation (ax^2 + bx + c) ==>'
    print 'a: %f, b: %f, c: %f' % (scipyQuad[0], scipyQuad[1], scipyQuad[2])
    profile('scipy_calc_quad', 'data')
    print('---------------------------')

    scipyGauss = scipy_calc_gaussian(data)
    print 'SciPy Gaussian Regression Equation (a * exp((-(x-b)^2)/(2*c^2)) ==>'
    print 'a: %f, b: %f, c: %f' % (scipyGauss[0], scipyGauss[1], scipyGauss[2])
    profile('scipy_calc_gaussian', 'data')
    print('---------------------------')