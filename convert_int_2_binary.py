#I want to write a program that converts an integer into a binary

#def int_binary(n):
	

n = 19
binary_list = list()

while n > 0:
	remainder = n % 2
	binary_list.insert(0, remainder)
	#binary_list.append(remainder)
	n = n/2 

print binary_list


