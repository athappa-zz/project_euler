#Project Euler #1

print '''
If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Note: Natural numbers are those used for counting and ordering
'''

natural_nums_3_5 = list()

print '''
Print the sum of the natural  
numbers that are multiples of 
3 or 5 below this number
''',
upper_bound = int(raw_input('>>> '))

for i in range(0,upper_bound):
	if i % 3 == 0 or i % 5 == 0:
		natural_nums_3_5.insert(0,i)
		
print sum(natural_nums_3_5)
	
	