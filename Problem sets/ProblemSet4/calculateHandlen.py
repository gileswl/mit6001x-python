def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """

    handlength = 0
    for element in hand:
        handlength = handlength + hand[element]
    return handlength