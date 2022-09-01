#!/usr/bin/python3
    
if __name__=="__main__":
    import sys
    
    x = len(sys.argv)
    b = (sys.argv)
    if x == 1:
        print("{} {}".format(0, "arguments."))
    if x  == 2:
        print("{} {}".format(1, "argument:"))
        print("{}: {}".format(1, b[1]))

    else:
        print("{} {}".format(((x) - 1), "arguments:"))
        for x in range(1, x):
            print("{}: {}".format(x, sys.argv[x]))
