#!/usr/bin/env python
#
# Project Euler Problem 3
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def checkIsPrime(num):
	if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
		return False
	
	for factor in range(11, num - 1):
		if factor % 2 == 0 or factor % 3 == 0 or factor % 5 == 0 or factor % 7 == 0:
			continue
		if num % factor == 0:
			return False
		
	return True

for i in range(1,5000000):
	if 600851475143 % i == 0 and checkIsPrime(i) == True:
		print "{} is the prime factor!".format(i)

