##
# @author : Francony Steven
# @brief : A set of generic functions for data management
##

# Input List
input_list = [1,2,3,4,-7]

# AVERAGING :
# average_above_zero function declaration
# @param input_list : the input list to be scanned.
# @throws an exception (ValueError) on an empty list
def average_above_zero(input_list):

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

# Call method
result = average_above_zero(input_list);

# Prepare and display message
message = "The average of positive element of {list_value} is {res} ".format(list_value = input_list , res = result);
print(message);


# TABLE MAXIMUM VALUE
# max_value function declaration
# @param input_list : the input list to be scanned.
# @throws an exception (ValueError) on an empty list
def max_value(input_list):

	# First check if provided list is not empty
	if len(input_list) == 0 :
		raise ValueError("Provided list is empty.");

	# Init max value
	max_val = input_list[0];

	# Average of positive elements of a list
	for item in input_list :
		# Select only positive items
		if max_val < item : 
			max_val = item

	return float(max_val);

# Call max_values method
myMax = max_value(input_list);

# Prepare & display message
message = "The maximum value of {list_value} is {max}".format(list_value = input_list, max = myMax)
print(message)


# RESERVE A TABLE
# reverse_table function declaration
# @param input_list : the input list to be scanned.
# @throws an exception (ValueError) on an empty list
def reverse_table(input_list):
	return input_list.reverse();

# Call method & display reverse table
reverse_table(input_list);
print(input_list)



