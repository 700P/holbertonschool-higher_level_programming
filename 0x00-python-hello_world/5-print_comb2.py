#!/usr/bin/python3

for x in range(100):
    if x == 99:
        print("{}".format(x))
    else:
        print(f"{x:02d}, ".format(x), end="")
