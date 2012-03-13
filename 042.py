#!/usr/bin/python
# -*- coding: utf-8 -*-

#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

#Answer:
	#162

from time import time; t=time()
from mathplus import isqrt

words = eval('(%s)' %(open('042-words.txt').read()))

M = 100
triangle_numbers = [n*(n+1)/2 for n in range(1, M)]

def is_triangle_word(s):
    num = sum((ord(c)-ord('A')+1) for c in s)
    if num in triangle_numbers: return True
    if num < triangle_numbers[-1]: return False
    n2 = num*8+1
    n = isqrt(n2)
    return n*n == n2

print(len(list(filter(is_triangle_word, words))))#, time()-t
