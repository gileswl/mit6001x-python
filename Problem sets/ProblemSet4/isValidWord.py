def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    currenthand = hand.copy()
    if word in wordList:
        for char in word:         
            if currenthand.get(char,0) == 0:
                return False
            updateHand(currenthand, char)
        return True
    else:
        return False
