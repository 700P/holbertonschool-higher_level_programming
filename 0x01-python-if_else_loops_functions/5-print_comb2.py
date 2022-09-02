#!/usr/bin/python3

for x in range(0, 100):
    if x == 99:
        print("99 \n".format(x))
    else:
        print(f"{x:02d}, ".format(x), end="")
