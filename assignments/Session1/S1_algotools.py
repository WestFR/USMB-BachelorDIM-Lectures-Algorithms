##
# @author : Francony Steven
#
# @brief : A set of generic functions for data management
##

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

# Input List
input_list = [1,2,3,4,-7]
result = average_above_zero(input_list);

# Prepare and display message
message = "The average of positive element of {list_value} is {res} ".format(list_value = input_list , res = result);
print(message);



def max_values(input_list):

	if len(input_list) == 0 :
		raise ValueError("Provided list is empty.");

	max_val = input_list[0];

	# Average of positive elements of a list
	for item in input_list :
		# Select only positive items
		if max_val < item :
			max_val = item

	return max_val;

myList = [1,3,7];

myMax = max_values(myList);
message = "My maximum value is : {max}".format(max = myMax)
print(message)


