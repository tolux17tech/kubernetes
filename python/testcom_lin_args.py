#!/usr/bin/python

import sys

x=sys.argv[1]
y=sys.argv[2]

print("The first command line argument is %s" %(x))
print("The second command line argument is %s" %(y))

#function definitions

def scheduled():
    
    print("Hi the scheduled function has been called")

    if x == 'scheduled':
        print("This script is scheduled")
        scheduled()
    else:
        print("This script is not scheduled")