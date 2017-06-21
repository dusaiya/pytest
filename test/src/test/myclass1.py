#!/usr/bin/python
# Filename: myclass1.py
import sys


def printDoc(sys, i):
    print sum.__doc__
    print 'The command line arguments are:'
    for i in sys.argv:
        print i
    
    print '\n\nThe PYTHONPATH is', sys.path, '\n'

def sum(x,y):
    '''Summation of two values
    '''
    return x+y
def sub(x,y):
    return x-y
v=dir(sys);
for i in v:
    print i
    #break
print v.__len__()

#printDoc(sys, i)
