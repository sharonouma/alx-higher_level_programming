#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("{:d} arguments.".format(num_args - 1))
    elif num_args == 2:
        print("{:d} argument:".format(num_args - 1))
    else:
        print("{:d} arguments:".format(num_args - 1))
    for i in range(1, num_args):
        print("{:d}: {:s}".format(i, sys.argv[i]))
