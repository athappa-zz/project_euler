#Project Euler #3

print '''
Instructions:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

#Idea 1. Find factors for any given N, then find the max(prime factor)
'''
n = 81
decrement = n
factors = list()


#find the factors of any given N	
while decrement > 0:
	if n % decrement == 0:
		factors.append(decrement)
	decrement = decrement - 1
print factors

#find the factors which are prime and print the max	
#amount of time to do this is too large
'''

#properties of a prime are that it is divisible by only itself and one
#also, for any given N, the largest prime factor will be less than the sqrt of N

n = 600851475143
i = 2 #we start with 2 because 2 is the smallest prime number

#Enter the loop as long as i*i is less than n
while i * i < n: 
	#as long as n % i divides evenly, we will continue to divide n by i
	while n % i == 0: #runs until
		n = n/i
	#once n does not divide evenly by i we exit the loop and increment i by 1
	i = i + 1 #incrementing fxn, increment i by 1

#if i * i is greater than n we won't be able to enter the first while loop
#and we will print n which was calculated in the previous iteration of the loop
print(n)







		
