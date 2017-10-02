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


# TABLE MINIMUM VALUE
# min_value function declaration
# @param input_list : the input list to be scanned.
# @throws an exception (ValueError) on an empty list
def min_value(input_list):

	# First check if provided list is not empty
	if len(input_list) == 0 :
		raise ValueError("Provided list is empty.");

	# Init max value
	min_val = input_list[0];

	# Average of positive elements of a list
	for item in input_list :
		# Select only positive items
		if min_val > item : 
			min_val = item

	return float(min_val);

# Call max_values method
myMin = min_value(input_list);

# Prepare & display message
message = "The minimum value of {list_value} is {min}".format(list_value = input_list, min = myMin)
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
# Function able to compute the corners' coordinates of an 'image' or 'matrix'

# Matrix processing libs
import numpy;

# Set a value in a specific cell
size_rows = 10;
size_cols = 10;
myMat = numpy.zeros([size_rows, size_cols], dtype = int);


# roi_bbox function declaration
# @param input_image : the input list of numpy to be scanned.
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

	bbox_coords = numpy.array([[xmin,ymin] , [xmax,ymin] , [xmin,ymax] , [xmax,ymax]])
	return bbox_coords

# Filling something in the matrix (the basic use)
# for row in range (0,5) :
#	for col in range (3,5) :
#		myMat[row, col] = 1

# Filling something in the matrix (a nicer way)
# myMat[0,0] = 1
myMat[0:6,3:9] = 1

# myMat[2:4,3:4] = numpy.ones([3,2])
# This line broke my code (doesn't support & compile on my MAC)

# Output coordinate matrix
#bbox_coords = numpy.zeros([4,2], dtype =int)
print (myMat)

myMatric = roi_bbox(myMat)
print("With index : \n {matrics}".format(matrics = myMatric));



# RANDOM ARRAY FILLING

# import random library
import random

# random_fill_sparse function declaration
# Function able to fill a defined number of table cells
# @param table : the table to be filled
# @param fill : the number of cells to be filled
# @throws an exception (ValueError)
def random_fill_sparse(table, fill):

    char = 'O'

    tablelength = table.shape[0]
    nbCells = tablelength * tablelength

    if fill > nbCells:
        raise ValueError("The number of cells to be filled is too high")
    
    for i in range(fill):
        filled = False

        while filled == False:
            random_x = random.randint(0,tablelength - 1)
            random_y = random.randint(0,tablelength - 1)
            if table[random_x][random_y] != char:
                table[random_x][random_y] = char
                filled = True
        
    return table

myMat = numpy.full([5,5],'',dtype='str')

# Call random_fill_sparse method @ display message
filled_table = random_fill_sparse(myMat,5)
print("Filled table : " + str(filled_table))



# REMOVE WHITESPACE

# remove_whitespace function declaration
# Function able to remove all whitespaces from a string
# @param input_list : the input list to be scanned.
def remove_whitespace(table):

    nbCharDeleted = 0

    for index,character in enumerate(table):
        if character == " ":
            table = table[:index - nbCharDeleted] + table[index-nbCharDeleted+1 :]
            nbCharDeleted += 1

    return table

myString = "There is a string !";
print("Here is the string with whitespaces : " + myString)

# Call remove_whitespace method & display message.
myString = remove_whitespace(myString)
print("Here is the string without whitespaces : " + myString)



# RANDOM ITEM SELECTION

# remove_whitespace function declaration
# Function able to randomly select items of a list
# @param list_in : the list to be shuffled
def shuffle(list_in):

    for index in reversed(xrange(len(list_in))):
        randomIndex = random.randint(0, index)
        indexValue = list_in[randomIndex]

        list_in[randomIndex] = list_in[index]
        list_in[index] = indexValue

    return list_in

# Initiliaze my list
myList = range(5)

# Display message before method call
print("List before shuffling : " + str(myList))

# Call shuffle method and display message
myList = shuffle(myList)
print("List after shuffling : " + str(myList))



# SORTING SELECTIVE

# MISSING QUESTIONS 

# sort_selective function declaration
# Function able to sort a list
# @param list_in : the list to be sorted
def sort_selective(list_in):

    for i in xrange(len(list_in) -1):
        minIndex = i
        for j in xrange(i, len(list_in)):
            if list_in[j] < list_in[minIndex]:
                minIndex = j

        if minIndex != i:
            tempValue = list_in[i]
            list_in[i] = list_in[minIndex]
            list_in[minIndex] = tempValue

    return list_in

# Initialize variable
myList = [10, 15, 7, 1, 3, 3, 9]

# Display message before method call
print("List before sorting : " + str(myList))

# Call sort_selective method and display message
myList = sort_selective(myList)
print("List after sorting : " + str(myList))



# SORTING BUBBLE

# MISSING QUESTIONS 

# sort_bubble function declaration
# Function able to sort a list
# @param list_in : the list to be sorted
def sort_bubble(list_in):
    
    permutations = True

    while permutations == True:
        permutations = False
        for i in xrange(1, len(list_in)):
            if list_in[i-1] > list_in[i]:
                tempValue = list_in[i]
                list_in[i] = list_in[i-1]
                list_in[i-1] = tempValue
                permutations = True

    return list_in

# Display message before method call
print("list before sorting : " + str(myList))

# Call sort_selective method and display messageb
myList = sort_bubble(myList)
print("list after sorting : " + str(myList))
