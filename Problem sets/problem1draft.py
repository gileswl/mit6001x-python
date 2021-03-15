# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#
#Number of vowels: 5

# input the string to parse
# uncomment this for interactive version

# s = str(input("Input a string of lower case letters: "))

# make a list of vowels

listOfVowels = ['a', 'e', 'i', 'o', 'u']

#set vowel count to zero

vowelcount = 0

#check if a character is a vowel 
for char in s:
    if char in listOfVowels:
        vowelcount = vowelcount+1

#print vowelcount
print("Number of vowels: " + str(vowelcount))