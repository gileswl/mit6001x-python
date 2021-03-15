L1 = [[1, 2], [3, 4], [5, 6, 7]]

print(L1)

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for elt in L:
        elt.reverse()

    L.reverse()

deep_reverse(L1)

print(L1)