##
# @author : Francony Steven
# @brief : A file testing
##

import pytest
import S1_algotools as algo

# Input List
input_list = [1,2,3,4,-7]
input_list1 = [2,4,8,10,12]

# AVERAGING
# Basic testing average function
def test_average_above_zero () :
	assert algo.average_above_zero(input_list) == 2.5
	assert algo.average_above_zero(input_list1) == 7.2

# TABLE MAXIMUM VALUE
# Basic max_value testing function
def test_max_value () :
	assert algo.max_value(input_list) == 4
	assert algo.max_value(input_list1) == 12

# TABLE MINIMUM VALUE
# Basic min_value testing function
def test_min_value () :
	assert algo.min_value(input_list) == -7
	assert algo.min_value(input_list1) == 2


# REVERSE TABLE
# Basic reverse_table testing function
def test_reverse_table () :
	assert algo.reverse_table(input_list) == [-7,4,3,2,1]



