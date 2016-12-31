#!/usr/bin/env python
###########################
# Made by: ?
# Site: ?
# version ?
###########################
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
LR = '\033[1;31m' # light red
LG = '\033[1;32m' # light green
LO = '\033[1;33m' # light orange
LB = '\033[1;34m' # light blue
LP = '\033[1;35m' # light purple
LC = '\033[1;36m' # light cyan
try:
	import os
	import sys
	# imports here
except ImportError, e:
	print R + "[You are missing required modules" + W
	print R + "Error: %s" % e + W
	exit(1)
while True:
    try:
        main = raw_input(LP + "Whatever>" + W)
        if main == "idk":
            print W + "code here"
	    # CODE HERE
        elif main == "idk1":
            print W + "some other code here"
	    # CODE HERE
        elif main == "idk2":
            print W + "some other code here"
	    # CODE HERE
        else:
            print W + "Else here"
	    # CODE HERE
    except:
        print R + "\nNot an option or you pressed Ctrl-C!"
        print "Exiting..."
        sys.exit()

