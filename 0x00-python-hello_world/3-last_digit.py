#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


state = ( "and is greater than 5", "and is 0", "and is less than 6 and not 0")
if number < 0:
    amp = (number % -10)
elif number > 0:
     amp = (number % 10)
else:
   number == 0
   amp = 0

if number > 5:
    print("Last digit of {} is {} {} ".format(number, amp, state[0]))
if number == 0:
    print("Last digit of {} is {} {} ".format(number, amp, state[1]))
if number < 6 & number > 0:
    print("Last digit of {} is {} {} ".format(number, amp, state[2]))
