#!/bin/python

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

diag = [ a[i][i] for i in range(len(a)) ]
counter_diag = [ row[-i-1] for i,row in enumerate(a) ]

sum = 0
for i in diag:
    sum = sum + i
for i in counter_diag:
    sum = sum - i

print abs(sum)
