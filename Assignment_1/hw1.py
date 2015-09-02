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

if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]
    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
