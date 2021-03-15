def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
import math

def closest_power(base,num):
    
    trueExponent = math.log(num, base)

    if round(trueExponent) > trueExponent:
        upperExponent = round(trueExponent)
        lowerExponent = round(trueExponent) - 1
    elif round(trueExponent) < trueExponent:
        upperExponent = round(trueExponent) +1
        lowerExponent = round(trueExponent)
    elif round(trueExponent) == trueExponent:
        upperExponent = round(trueExponent)
        lowerExponent = round(trueExponent)

    if abs((base**upperExponent)-num) > abs((base**lowerExponent) - num):
        closestExponent = int(lowerExponent)
    elif abs((base**upperExponent)-num) < abs((base**lowerExponent) - num):
        closestExponent = int(upperExponent)
    elif abs((base**upperExponent) - num) == abs((base**lowerExponent) - num):
        closestExponent = int(lowerExponent)
    
    return(closestExponent)

base = int(input("Enter a base to use, integer > 1: "))
num = int(input("Enter a target number, integer > 0: "))

closestExponent = closest_power(base, num)

print(str(closestExponent))