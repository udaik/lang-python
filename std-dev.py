from random import randint
from math import sqrt
import numpy

cardinal = 10000000

min = 0
max = 100

rand = []

for i in range(cardinal):
    rand.append(randint(min, max))

# print rand

sum = 0
for i in rand:
    sum = sum + i

mean = sum/len(rand)
print(mean)

variance = 0
for i in rand:
    variance = variance + pow(i-mean, 2)

variance = variance/len(rand)
print(sqrt(variance))

arr = numpy.array(rand)
print(numpy.mean(arr, axis=0))
print(numpy.std(arr, axis=0))
