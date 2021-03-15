#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

# input the string to parse
# uncomment this for interactive version

# s = str(input("Input a string of lower case letters: "))

# get the length of the string s

stringlength = len(s)

# start from 0

bobcount = 0
currentchar = 0

# moves along the string until you get within 2 characters of the end
while currentchar < (stringlength -2):
# checks if this character and the next two are the string 'bob'
    if s[currentchar:currentchar+3] == 'bob':
        bobcount = bobcount+1
    currentchar = currentchar+1

print('Number of times bob occurs is: ' + str(bobcount))