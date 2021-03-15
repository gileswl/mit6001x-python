#  Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)
# This function takes in a dictionary and returns a list.

aDict = {'key6':'1', 'key2':'2', 'key3':'7', 'key5':'3', 'key4':'4'}

# initialise an empty list

uniqueKeys = []

# for each key, get its corresponding value

for word in aDict:
    foundCount = 0
    currentKey = word
    for elt in aDict.values():
        if elt == aDict[currentKey]:
            foundCount +=1
    if foundCount == 1:
        uniqueKeys.append(currentKey)

uniqueKeys.sort()

print(uniqueKeys)

# for each key, compare its value to the value of all other keys
# if it doesn't match any, append the key to the list
# sort the list