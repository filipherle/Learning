import os
import sys
import pip
try:
    abc, lol = raw_input('Enter two things: ').split()
    if lol == "":
        print "No second thing"
    else:
        print "Second thing entered"
except ValueError:
    print "Error"