#!/bin/python

import sys

def simpleArraySum(n, ar):
    # Complete this function
    sum = 0
    for i in ar:
        sum = sum + i
    return sum

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
print ar
result = simpleArraySum(n, ar)
print(result)
