#!/usr/bin/env python3

def fizzbuzz(x):
    print(x)

    for x in range(100):
        if x % 3 == 0:
            print(Fizz)
        if x % 5 == 0: 
            print(Buzz)
        if x % 5 & 3:
            print(FizzBuzz)
            return fizzbuzz()
