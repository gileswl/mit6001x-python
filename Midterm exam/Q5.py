# Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗103+2∗102+3∗101+4∗100.

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    # return a function

    #initalize list of functions of x
    k = len(L)    
    
    def f1(x):
        runningtotal = 0
        
        for n in range(k):
            subtotal = L[n] * (x**(k-(n+1)))
            runningtotal = runningtotal + subtotal
        
        return runningtotal

    return f1

print(general_poly([1,2,3,4])(10))
    