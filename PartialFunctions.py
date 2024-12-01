
"""
Edit the function provided by calling partial() and replacing
the first three variables in func(). Then print with
the new partial function using only one input
variable so that the output equals 60
"""

#Following is the exercise, function provided:
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

#Here I am preloading the func functions call's first 3 parameters
#With default values and assigning into another function pointer func3

func3 = partial(func, 10, 2, 2)

#Here I am using func3 to call func with 3 parameters already passed as part of partial call
print(func3(10))
