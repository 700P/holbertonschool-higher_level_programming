#!/usr/bin/env python3
import random

number = random.randint(-10, 10)
x = number

if x < 0: 
    print("{} is negative".format(x));
if x == 0:
    print("{} is zero".format(x));
if x > 0:
    print("{} is positive".format(x));
