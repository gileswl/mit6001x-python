# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
# Hints:
#
#    You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.
#
#    Consider using lower() to convert user input to lower case. For example:
#
#    guess = 'A'
#    guessInLowerCase = guess.lower()
#
#    Consider writing additional helper functions if you need them!
#
#    There are four important pieces of information you may wish to store:
#        secretWord: The word to guess.
#        lettersGuessed: The letters that have been guessed so far.
#        mistakesMade: The number of incorrect guesses made so far.
#        availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

# At the start of the game, let the user know how many letters the secretWord contains.

# for testing - exclude from hangman function definition
secretWord = "apple"

#functions defined elsewhere for reference - exclude from hangman function definition 

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isWordGuessed = True

    for char in secretWord:
        if (char in lettersGuessed) == False:
            isWordGuessed = False

    return(isWordGuessed)

def getGuessedWord(secretWord, lettersGuessed):
    currentGuess = str()

    for char in secretWord:
        if (char in lettersGuessed) == True:
            currentGuess = currentGuess + str(char) + ' '
        else:
            currentGuess = currentGuess + '_' + ' '
            
    return(currentGuess)

def getAvailableLetters(lettersGuessed):
    import string
    
    lettersRemaining = str()
    for char in string.ascii_lowercase:
        if (char in lettersGuessed) == False:
            lettersRemaining = lettersRemaining + char
    
    return(lettersRemaining)

# begin hangman function definition

# def hangman(secretWord):

secretWordLength = str(len(secretWord))

guessesPermitted = 8
wrongGuessesMade = 0

print("Welcome to the game Hangman!")
print("I am thinking of a word that is", secretWordLength, "letters long.")
print("------------")

lettersGuessed = str()

while True:
    print("You have", (guessesPermitted - wrongGuessesMade), "guesses left.")
    print("Available letters:", str(getAvailableLetters(lettersGuessed)))
    guess = input("Please guess a letter: ")
    guessInLowerCase = guess.lower()
    if (guessInLowerCase in str(getAvailableLetters(lettersGuessed))) == False:
        print("Oops! You've already guessed that letter: ", str(getGuessedWord(secretWord, lettersGuessed)))
        print("------------")
    elif (guessInLowerCase in str(secretWord)) == True:
        lettersGuessed = lettersGuessed + guessInLowerCase
        print("Good guess: ", str(getGuessedWord(secretWord,lettersGuessed)))
        print("------------")
        if (isWordGuessed(secretWord, lettersGuessed)) == True:
            print("Congratulations, you won!")
            break
    elif (guessInLowerCase in str(secretWord)) == False:
        lettersGuessed = lettersGuessed + guessInLowerCase
        wrongGuessesMade += 1
        print("Oops! That letter is not in my word: ", str(getGuessedWord(secretWord,lettersGuessed)))
        print("------------")
        if (wrongGuessesMade < guessesPermitted) == False:
            print("Sorry, you ran out of guesses. The word was", str(secretWord), ".")
            break
    else:
        print("Something went wrong the with the code!")
        break

