__author__ = 'Suman'

import Tkinter
import tkFileDialog
import csv


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
    


if __name__ == "__main__":
    model = calc_lsr(read_datapoints())
    print 'Regression Equation is ==>'
    print 'y-hat = %f + %f * x' % (model[0], model[1])
    print 'Here, b0 [Y-intercept] : %f,  b1 [Slope]: %f' % (model[0], model[1])
    
