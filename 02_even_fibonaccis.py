#Project Euler #2

print '''
Instructions:
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
'''

#Initialize the list to which we will add the fibonacci #s that fit our critera
fib_nums = list()

def fibonacci(n):
	"print a fibonacci series up to n"
	a, b = 0, 1
	while b < n:
		#print b,
		a, b = b, a+b
		if b % 2 == 0:
			print b
			fib_nums.append(b)
fibonacci(4000000)
print 'the sum of the fibonacci numbers between 1 and 4mm is', sum(fib_nums)

