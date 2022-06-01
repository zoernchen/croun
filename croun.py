import math
from decimal import *

"""
rounding numbers:
    for n>0:    p>=5 round up
                p<5  round down
    for n<0:    ignore the minus --> do the same as for n>0 --> add the minus again
"""

def rnd(n, decimals=0):
    if n>0:
        multiplier = 10 ** decimals
        m = math.floor(n * multiplier + 0.5) / multiplier
        return m
    elif n<0:
        n = -n
        multiplier = 10 ** decimals
        m = math.floor(n * multiplier + 0.5) / multiplier
        return -m
    else:
        return 0

"""
rounding numbers down:
    for n>0 round down
    for n<0 round down 
down meaning towards the 0
"""
def drnd(n, decimals=0):
    if n>0:
        multiplier = 10**decimals
        m = math.floor(n * multiplier) / multiplier
        return m
    elif n<0:
        n = -n
        multiplier = 10**decimals
        m = math.floor(n * multiplier) / multiplier
        return -m
    else:
        return 0


"""
rounding numbers according to needs in physics:
    first specified digit: d
    if 0<d<3 (d=1, d=2): decimals=1
    if d>3: decimals=0
round with rnd(n,decimals=0) accordingly

CAUTION!
THIS SCRIPT MAY NOT BE PERFECT
THERE MIGHT BE SLIGHT ROUNDING ERRORS
"""

def prnd(n):
    decimals = 0
    while abs(n)<1:
        decimals = decimals + 1
        n = Decimal(n*10)
    while abs(n)>10:
        decimals = decimals -1
        n = Decimal(n*10)   
    if 10>abs(n)>=1:
        if 0<int(n)<3:
            m =  drnd(n, 4)
            k= 1 + decimals
        else:
            m = drnd(n,3)
            k= 0 +decimals
        r = 10**(0 - decimals)
        if n>0:
            if decimals == 0:
                return int(m)
            else:
                return rnd(m * r, k)
        if n<0:
            if decimals == 0:
                return -int(m)
            else:
                return rnd(-m * r, k)
        else:
            return 0
    

# TEST FOR rnd
#print("(two decimals) 3.455 rounds to", rnd(3.455, 2), "(should be 3.46)")
#print("(one decimal) 0 rounds to", rnd(0,1), "(should be 0)")
#print("(one decimal) -0.65 rounds to", rnd(-0.65,1), "(should be -0.7)")

#TEST FOR drnd
#print("(1 decimal) 3.99 rounds to", drnd(3.99, 1), "(should be 3.9)")
#print("(one decimal) -5.35 rounds to", drnd(-5.35, 1), "(should be -5.3)")
#print("(four decimals) 0.65 rounds to", drnd(0.65, 4), "(should be 0.65)")
#print(drnd(2.35, 4))

# TEST FOR prnd
#print("0.00235 rounds to", prnd(0.00235), "(should be 0.0024)")
#print("0.65 rounds to", prnd(0.65), "(should be 0.7)")
#print("3.04 rounds to", prnd(3.04), "(should be 3)")
#print("0.234995 rounds to", prnd(0.234995), "(should be 0.23)")