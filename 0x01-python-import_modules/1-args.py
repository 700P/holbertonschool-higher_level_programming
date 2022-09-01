#!/usr/bin/python3
import sys

"""
def titles(*inns):
    for inns in sys.stdin:
        print(len(inns))

"""

print(len(sys.argv) -1)

for x in range (1, len(sys.argv)):
    print((sys.argv[x]))

