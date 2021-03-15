def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #If s1 is empty, add the remainder of s2 and return it
            # loopcount += 1
            # print("loop number:", str(loopcount))
            # print("Adding remainder of s2:", str(s2))
            # print("Nearly done!")
            # print("Returning:", str(out + s2))
            return (str(out + s2))
            
        if s2 == '':
            #if s2 is empty, add the remainder of s1 and return it
            # loopcount += 1
            # print("loop number:", str(loopcount))
            # print("Adding remainder of s1:", str(s1))
            # print("Nearly done!")
            # print("Returning:", str(out + s1))
            return (str(out + s1))
            
        else:
            #If neither is empty, get the first value of each and go into the loop again to get the second value
            # loopcount += 1
            # print("loop number:", str(loopcount))
           #print("Adding s1[0] and s2[0]:", str(s1[0]), "and", str(s2[0]))
            #print("calling helpLaceStrings again!")
            #print("setting out to:", (str(s1[0] + s2[0])), ", and the next call")
            return (str(helpLaceStrings((s1[1:]), s2[1:], out+s1[0]+s2[0])))

print(helpLaceStrings('cmlaknfaionfalkscnv qeofrt', '12831094honc3178g', ''))