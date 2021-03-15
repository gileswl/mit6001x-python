# Course Week 1: Python Basics Problem Set 1 Problem 3
# 
# It finds the longest contiguous string of alphabetical string of characters in a string of lower case characters (earliest string in case of a tie)

# store s in my own variable

# input the string to parse

# uncomment below for interative version

# s = str(input("Input a string of lower case letters: "))

# test string
# s = "zyx"

teststring = s

# setting up the alphabet index
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_index = 0
for char in alphabet:
    vars()[alphabet[alphabet_index]] = alphabet_index
    alphabet_index += 1
# check index 
# print(a)
# check index print(z)


# get ready to step through the input string from the beginning
i = 0
# for the first character, just set up the output string
s_longestknown = teststring[i]
# Start keeping track of the current read
s_currentread = teststring[i]
#step forward one character
i += 1

#If I'm still within the input string, keep checking
while i < len(teststring):
    alphabet_compare = 0
    current_char_index = 0
    # figure our the current character's position in the alphabet
    while alphabet_compare < 26:
        if (teststring[i] == alphabet[alphabet_compare]):
            current_char_index = alphabet_compare
            break
        else:
            alphabet_compare += 1
    # figure out the previous character's alphabetical index
    alphabet_compare = 0
    prev_char_index = 0
    while alphabet_compare < 26:
        if (teststring[i-1] == alphabet[alphabet_compare]):
            prev_char_index = alphabet_compare
            break
        else:
            alphabet_compare += 1
    # check if the current character is in alphabetical order with the previous character
    if current_char_index >= prev_char_index:
        # if it is, append it to the current read
        s_currentread = s_currentread + teststring[i]
        # if it isn't, reset the current read to this character
    else:
        s_currentread = teststring[i]
    #check whether the current read is longer than the longest known
    if len(s_currentread) > len(s_longestknown):
        #if so, update the longest known
        s_longestknown = s_currentread
    #move forward to the next character
    i +=1
    #end of while loop
print("Longest substring in alphabetical order is: " + str(s_longestknown))