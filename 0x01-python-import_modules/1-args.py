#!/usr/bin/python3
    
if __name__=="__main__":
    import sys

    x = (sys.argv)
    a = len(sys.argv)
    s = range(1, x)

    if a == 0:
        print("{} {}".format(0, "arguments."))
    if a == 1:
        print("{} {}".format(1, "argument:"))
        print("{}: {}".format(a, x))
    elif a == 2:
        print("{} {}".format(a, "arguments:"))
        print("{}: {}".format(s, sys.argv[s]))
