# Write a recursive procedure, called laceStringsRecur(s1, s2), which also laces together two strings. Your procedure should not use any explicit loop mechanism, such as a for or while loop. We have provided a template of the code; your job is to insert a single line of code in each of the indicated places.

# For this problem, you must add exactly one line of code in each of the three places where we specify to write a line of code. If you add more lines, your code will not count as correct.

# Here is the template you will fill in, for reference:

# s1 = str('abcdefg')
# s2 = str('123456')

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # print("s1 is:", s1)
    # print("s2 is:", s2)
    #counter
    
    # loopcount = 0
    
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #If s1 is empty, add the remainder of s2 and return it
            # loopcount += 1
            # print("loop number:", str(loopcount))
            #print("Adding remainder of s2:", str(s2))
            #print("Nearly done!")
            #print("Returning:", str(out + s2))
            return str(out + s2)
            
        if s2 == '':
            #if s2 is empty, add the remainder of s1 and return it
            # loopcount += 1
            # print("loop number:", str(loopcount))
            #print("Adding remainder of s1:", str(s1))
            #print("Nearly done!")
            #print("Returning:", str(out + s1))
            return str(out + s1)
            
        else:
            #If neither is empty, get the first value of each and go into the loop again to get the second value
            # loopcount += 1
            # print("loop number:", str(loopcount))
           #print("Adding s1[0] and s2[0]:", str(s1[0]), "and", str(s2[0]))
            #print("calling helpLaceStrings again!")
            #print("setting out to:", (str(s1[0] + s2[0])), ", and the next call")
            return (str(helpLaceStrings((s1[1:]), s2[1:], out+s1[0]+s2[0])))
    return helpLaceStrings(s1, s2, '')

    #    print("the return from helpLaceStrings is:", str(helpLaceStrings('cmlaknfaionfalkscnv qeofrt', '12831094honc3178g', '')))

    # print("the return from laceStringsRecur is:", str(

print (laceStringsRecur('abcde', 'adsa'))




