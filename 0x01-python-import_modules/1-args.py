#!/usr/bin/python3
    
if __name__=="__main__":
    import sys

    b = (sys.argv)
    a = len(sys.argv)

    if a == 0:
        print("{} {}".format(0, "arguments."))
    if a == 1:
        print("{} {}".format(1, "argument:"))
        print("{}: {}".format(1, b[1]))
    elif a == 2:
        print("{} {}".format(((a) - 1), "arguments:"))
        for x in range(1, a):
            print("{}: {}".format(x, sys.argv[x]))
