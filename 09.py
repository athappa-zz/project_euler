#Project Euler #9

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which,
a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Process:
1. Looked at clarifying Stack post: http://stackoverflow.com/questions/2769842/project-euler-9-understanding
2. Saw a comment about simplifying the equation
3. Took 2 equations: (a+b+c)=1000 and a**2+b**2=c**2 and tried to combine

Math:
c = 1000 - a - b
c**2 = a**2 + b**2
'''
#Import modules
import time




def pythagoras(n):
	for a in range(1,n):
		for b in range(1,n-a):
			c = n - a - b
			if a**2 + b**2 == c**2:
				print 'the triples are', a, b,'and', c
				return a*b*c 



print pythagoras(1000)





 
#start = time.time()
#function call
#elapsed = (time.time() - start)
 

