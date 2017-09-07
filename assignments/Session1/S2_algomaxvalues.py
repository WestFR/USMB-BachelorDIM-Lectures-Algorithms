##
# @author : Francony Steven
#
# @brief : A set of generic functions for data management
##

def max_values(input_list):

	# Variables
	positive_values_sum = 0
	positive_values_count = 0
	first_item = input_list[0]

	# Average of positive elements of a list
	for item in input_list :
		# Select only positive items
		if item > 0 :
			positive_values_sum += item
			positive_values_count += 1
		elif item == 0 :
			print("This value is null : " + str(item));
		else :
			print("This value is not positive : " + str(item));
		
	# Compute the final average
	average = float(positive_values_sum / float(positive_values_count));
	return float(average);

# Input List
input_list = [1,2,3,4,-7]
result = average_above_zero(input_list);

# Prepare and display message
message = "The average of positive element of {list_value} is {res} ".format(list_value = input_list , res = result);
print(message);