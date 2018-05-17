#!/usr/bin/python

def max_of_num(x,y,z):
    max=x
    if (y>x)and(y>z):
        max=y
    elif(z>max)and(z>y):
        max=z
    return max

print (max_of_num(78,45,34))