#Project Euler #10

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Pseudocode:

find primes up to n

for all numbers a: from 2 to sqrt(n)
	if a is unmarked THEN
		a is prime
		for all multiples of a (a<n)
			mark multiples as composite
All unmarked numbers are prime
'''


def primes(n):
	sqrtn = int(round((n**0.5)))
	nums = xrange(2, n) 
	for i in xrange(2, sqrtn): 
		nums = filter(lambda x: x == i or x % i, nums)
	return nums, sum(nums)
print primes(2000000)

'''
from itertools import takewhile
def eratosthenes():
    #Yields the sequence of prime numbers via the Sieve of Eratosthenes.
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

print sum(takewhile(lambda x: x < 2000000, eratosthenes()))
'''