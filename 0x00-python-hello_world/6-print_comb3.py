#!/usr/bin/env python3

for x in range(10):
    for a in range(10):
        if a > x:
            if x == 8 and a == 9:
                print("{}{}".format(x, a))
            else:
                print("{}{}".format(x, a), end=", ")
