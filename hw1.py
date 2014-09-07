#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
import random #Needed for my attempt at the quicksort algorithm.
def sortwithloops(input):
    '''This sort is based off of things I found when researching the 
    quicksort algorithm. The sort takes a list as an input and
    sorts the list by randomly selecting a pivot and then sorting
    the list into two groups based on their comparison to the pivot.
    '''
    #Three lists used to store the results of the comparisons.
    lesser = []
    equal = []
    greater = []
    
    if len(input) > 1:
        pivot = random.choice(input)
        #For loop to sort the list into three groups based on their
        #comparison to the pivot.
        for i in input:
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
        return input #return a value
	
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input): 
    '''Takes a list and uses the list sorted operator to sort
    the list.
    '''
    list_sort = sorted(input)
    return list_sort

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    '''Takes a list and a value and uses a for loop to do a 
    linear search for the value is in the list.
    ''' 
    for item in input:
        if item == value:
            return True
    return False

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    '''Takes a list and value and uses the in list operator to 
    check if the value is in the list.
    '''
    if value in input:
        return True
    else:
        return False #return a value	

if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]	

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
