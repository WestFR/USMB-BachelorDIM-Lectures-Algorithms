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

	lastidx = len(input_list)

	for idx in xrange (len(input_list) /2) :
		lastidx -= 1
		poppod =  input_list[idx]

		input_list[idx] = input_list[lastidx]
		input_list[lastidx] = poppod;

	# OR SIMPLY : return input_list.reverse();

# Call method & display reverse table
reverse_table(input_list);
message = "My reverse table is : {list_value}".format(list_value = input_list);
print(message)


# BOUDING BOX

# Matrix processing libs
import numpy;

# Set a value in a specific cell
size_rows = 10;
size_cols = 10;
myMat = numpy.zeros([size_rows, size_cols], dtype = int);

# roi_bbox function declaration
# @param input_image : the input list of numpy to be scanned.
#
def roi_bbox(input_image) :

	# Set values for bouding box
	xmin = size_cols;
	xmax = 0;
	ymin = size_rows;
	ymax = 0;

	for x in range(size_cols) :
		for y in range (size_rows) :
			if input_image[x , y] > 0 :
				if xmin > x :
					xmin = x;
				if xmax < x :
					xmax = x;
				if ymin > y :
					ymin = y;
				if ymax < y :
					ymax = y;

	bbox_coords = numpy.array([[ymin,xmin] , [ymin,xmax] , [ymax,xmin] , [ymax,xmax]])
	return bbox_coords

# Filling something in the matrix (the basic use)
# for row in range (0,5) :
#	for col in range (3,5) :
#		myMat[row, col] = 1

# Filling something in the matrix (a nicer way)
myMat[1,3] = 1
myMat[2:4,4:9] = 1

# myMat[2:4,3:4] = numpy.ones([3,2])
# This line broke my code (doesn't support & compile on my MAC)

# Output coordinate matrix
#bbox_coords = numpy.zeros([4,2], dtype =int)
print (myMat)

myMatric = roi_bbox(myMat)
print(myMatric);




