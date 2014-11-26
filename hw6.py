__author__ = 'Erik Nylander'

import numpy as np
import random
import timeit


def sortwithloops(lst):
    '''This sort is based off of things I found when researching the
    quicksort algorithm. The sort takes a list as an input and
    sorts the list by randomly selecting a pivot and then sorting
    the list into two groups based on their comparison to the pivot.
    '''
    #Three lists used to store the results of the comparisons.
    lesser = []
    equal = []
    greater = []

    if len(lst) > 1:
        pivot = random.choice(lst)
        #For loop to sort the list into three groups based on their
        #comparison to the pivot.
        for i in lst:
            if i < pivot:
                lesser.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        #The return calls the function on the lists of values greater and
        #lesser than the pivot and concatenates the results with list
        #equal to the pivot. I found this way of handling the return while
        #researching the algorithm.
        return sortwithloops(lesser) + equal + sortwithloops(greater)

    else:
        return lst #return a value


def sortwithoutloops(lst):
    '''Takes a list and uses the list sorted operator to sort
    the list.
    '''
    return sorted(lst)


def numpysort(array):
    '''
    Sorts using the NumPy sort function.
    :param array: np.array to be sorted.
    :return: sorted array
    '''
    return np.sort(array)


def searchwithloops(lst, value):
    '''Takes a list and a value and uses a for loop to do a
    linear search for the value is in the list.
    '''
    for item in lst:
        if item == value:
            return True
    return False


def searchwithoutloops(lst, value):
    '''Takes a list and value and uses the in list operator to
    check if the value is in the list.
    '''
    if value in lst:
        return True
    else:
        return False


def numpysearch(lst, value):
    '''
    Searches for a given value in the list.
    :param lst: np.array to be searched through
    :param value: value to be found in the array
    :return: True or false based on the search
    '''
    if len(np.where(lst == value)[0]) > 0:
        return True
    else:
        return False


def timesort(func, lst, n=1000000):
    '''
    Prints the timing generated from the timeit function for the sort functions.
    :param func: function to be tested as a string
    :param lst: variable name for the list of values to be sorted as a string
    :param n: number of iterations of the timing function, defaults to 1,000,000
    :return: none
    '''
    t = timeit.timeit("%s(%s)" % (func, lst), setup="from __main__ import %s, %s" % (func, lst), number=n)
    print "Timing: %d loops in %f seconds" %(n, t)


def timesearch(func, lst, value, n=1000000):
    '''
    Prints the timing generated from the timeit function for the search functions.
    :param func: function to be tested as a string
    :param lst: variable name for the list of values to be searched through as a string
    :param value: value to be found as an integer
    :param n: number of iterations of the timing function, defaults to 1,000,000
    :return: none
    '''
    t = timeit.timeit("%s(%s, %d)" % (func, lst, value), setup="from __main__ import %s, %s" % (func, lst),
                      number=n)
    print "Timing: %d loops in %f seconds" %(n, t)


if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]
    arr = np.array(L)

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print numpysort(arr)
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
    print numpysearch(arr, 5)
    print numpysearch(arr, 11), '\n'

    print 'Sorting:'
    print '---------------------------'
    print 'Sorting with Iteration:'
    timesort('sortwithloops', 'L')
    print ''
    print 'Sorting with Built-In Functions:'
    timesort('sortwithoutloops', 'L')
    print ''
    print 'Sorting with NumPy:'
    timesort('numpysort', 'arr')
    print ''

    print 'Searching:'
    print '---------------------------'
    print 'Searching with Iteration, Value in List:'
    timesearch('searchwithloops', 'L', 5)
    print''
    print 'Searching with Iteration, Value not in List:'
    timesearch('searchwithloops', 'L', 11)
    print''

    print 'Searching with Built-In Functions, Value in List:'
    timesearch('searchwithoutloops', 'L', 5)
    print ''
    print 'Searching with Built-In Functions, Value not in List:'
    timesearch('searchwithoutloops', 'L', 11)
    print''

    print 'Searching with NumPy, Value in List:'
    timesearch('numpysearch', 'L', 5)
    print ''
    print 'Searching with NumPy, Value not in List:'
    timesearch('numpysearch', 'L', 11)