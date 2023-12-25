import numpy as np
from itertools import product as iters

#
def flood_fill(ar, i ,j, val):
    ar[i, j] = val
    ar = fill(ar, i, j, val)
    return ar
#optimize this by remembering which cells have been visited
#breadth first search
def fill(ar, i, j, val):
    for k, l in iters(range(-1, 2), repeat=2):
        if np.abs(k) + np.abs(l) != 2 and wbc(ar, i + k , j + l):
            if ar[i+k, j+l] == 0:
                ar[i+k, j+l] = val
                ar = fill(ar, i+k, j+l, val)
    return ar
#use a catalogue of allowed indices combinations
#i tensor j to make it
# something like 2**i + 4**j
"""
for a00, a01, a10, a11, b00, b01, b10, b11 in iters([0, 1], repeat = 8):
        ar = np.array([[a00, a01],[a10, a11]])
        br = np.array([[b00, b01],[b10, b11]])
        #Implemented deterministic (delta) distribution
        #flatten μ
        #μ = np.reshape(μ, (256, 1))
        #HERE WAS THE PROBLEM
        #WAS USING WRONG BINARY FUNCTION TO ADRESS THE CONTENTS
        indi = 1*a00+2*a01+4*a10+8*a11+16*b00+32*b01+64*b10+128*b11
"""
#within border check
def wbc(ar, i, j):
    flag = False
    x, y = np.shape(ar)
    if (-1 < i < x ) and ( -1 < j < y):
        flag = True
    return flag

#on border check
def obc(ar, i, j):
    flag = False
    size = np.shape(ar)
    if ( i == 0 ) or ( i == size[0] - 1):
        if ( j == 0 ) or ( j == size[1] - 1):
            flag = True
    return flag

#Calculate the volume and if it spills out
def calc(ar, val):
    flag = False
    s = np.shape(ar)
    vol = 0
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            if ar[i, j] == val:
                vol +=1
                if obc(ar, i, j):
                    flag = True
    return flag, vol

#Reduce level
def rlevel(ar_in, level):
    arr = ar_in - level
    arr[ arr < 0] = 0
    return arr