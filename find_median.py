# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.
#sort the list containing x,y,z
#if they are all different numbers, return y
#if two of them are the same, return the two that are the same
#if the list is even, we would want to divide the two 



def median(x,y,z):
	global number_list, median
	number_list = sorted([x,y,z])

	if len(number_list) % 2 == 0:
		number_list_index = number_list[(len(number_list)/2)-1:(len(number_list)/2)+1]
		median = number_list_index[1]/number_list_index[0]
		return median
	else:
		median = number_list[len(number_list)/2]
		return median
		
median(1,2,50)
print median

