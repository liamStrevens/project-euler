#!/usr/bin/python
# -*- coding: utf-8 -*-

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#Answer:
	#4179871

from time import time; t = time()

M=28123

M+=1
d = [1] * M
d[0] = 0
for i in range(2, (M+1)//2):
    for j in range(i*2, M, i):
        d[j] += i
flags = [(d[i] > i) for i in range(M)]
abundants = [i for i in range(M) if d[i] > i]

s = M*(M-1)//2
for i in range(M):
    m = i//2
    for j in abundants:
        if j > m: break
        if flags[i-j]:
            s -= i
            break
print(s)#, time()-t
