__author__ = "Suman"

import numpy as np
import timeit

#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    """sort a list of objects"""
    left=[]
    splitpoint=[]
    right=[]

    if len(input) > 1:
        pivot = input[0]
        for elem in input:
            if elem < pivot:
                left.append(elem)
            elif elem == pivot:
                splitpoint.append(elem)
            else:
                right.append(elem)
        return sortwithloops(left)+splitpoint+sortwithloops(right)
    else:
        return input

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):
    return sorted(input)

def sortwithnumpy(array):
    '''
    Sort with the NumPy sort function.
    :inputs: array to be sorted.
    :return: sorted array
    '''
    return np.sort(array)

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    """ Find the value in the input and return True if found, else False  """
    lb = 0
    ub = len(input)
    while True:
        if lb == ub:   # If there is no region of interest (ROI)
           return False

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = input[mid_index]


        # compare to the value?
        if item_at_mid == value:
            return True      # Found it - the index is mid_index!
        if item_at_mid < value:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    return value in input


def searchwithnumpy(input, value):
    '''
    Searches for a given value in the list.
    :Inputs
    :input - np.array to be searched
    :value - value to be found in the array
    :return: boolean , True if found else False
    '''
    #in1d - Test whether each element of a 1-D array is also present in a second array
    #Returns a boolean array the same length as ar1 that is True where an element of ar1 is in ar2 and False otherwise.
    foundarray = np.in1d(input, [value])
    return np.count_nonzero(foundarray) > 0

def timesort(func, lst, n=10000):
    '''
    Prints the timing generated from the timeit function for the sort functions.
    :Inputs:
    :func: function to be tested as a string
    :lst: variable name for the list of values to be sorted as a string
    : n: number of iterations of the timing function, defaults to 1,000,000
    :return: none
    '''
    t = timeit.timeit("%s(%s)" % (func, lst), setup="from __main__ import %s, %s" % (func, lst), number=n)
    print "Timing: %d iterations in %f seconds" %(n, t)

def timesearch(func, lst, value, n=10000):
    '''
    Prints the timing generated from the timeit function for the search functions.
    :Inputs:
    :func: function to be tested as a string
    :lst: variable name for the list of values to be searched.
    :value: value to be found as an integer
    :n: number of iterations of the timing function - defaults to 1,000,000
    :return: none
    '''
    t = timeit.timeit("%s(%s, %d)" % (func, lst, value), setup="from __main__ import %s, %s" % (func, lst), number=n)
    print "Timing: %d iterations in %f seconds" %(n, t)
    
    
if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]
    arr = np.array(L)
    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithnumpy(arr)
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
    print searchwithnumpy(arr, 5)
    print searchwithnumpy(arr, 11)
    
    print 'Sorting:'
    print '---------------------------'
    print 'Sort using Iteration:'
    timesort('sortwithloops', 'L')
    print ''
    print 'Sort using Built-In Functions:'
    timesort('sortwithoutloops', 'L')
    print ''
    print 'Sort using numpy:'
    timesort('sortwithnumpy', 'arr')
    print ''
    
    print 'Searching:'
    print '---------------------------'
    print 'Search using Iteration, Value in List:'
    timesearch('searchwithloops', 'L', 5)
    print''
    print 'Search using Iteration, Value not in List:'
    timesearch('searchwithloops', 'L', 11)
    print''
    
    print 'Search using Built-In Functions, Value in List:'
    timesearch('searchwithoutloops', 'L', 5)
    print ''
    print 'Search using Built-In Functions, Value not in List:'
    timesearch('searchwithoutloops', 'L', 11)
    print''

    print 'Search using numpy, Value in List:'
    timesearch('searchwithnumpy', 'L', 5)
    print ''
    print 'Search using numpy, Value not in List:'
    timesearch('searchwithnumpy', 'L', 11)
