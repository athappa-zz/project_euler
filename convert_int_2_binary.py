#I want to write a program that converts an integer into a binary

#def int_binary(n):

input_sign = '>>> '	

print '''
Type in an integer you would like to be converted into a binary
''' 
n = int(raw_input(input_sign))
 
#n = 19
binary_list = list()

while n > 0:
	remainder = n % 2
	binary_list.insert(0, remainder)
	#binary_list.append(remainder)
	n = n/2 

print binary_list


