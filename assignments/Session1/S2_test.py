##
# @author : Francony Steven
# @brief : A file testing
##

import pytest
import S1_algotools as algo

# Fixtures region
@pytest.fixture
def int_fixture ():
	return [1,2,3,4,-7]

@pytest.fixture
def positive_list_fixture () :
	return [2,4,8,10,12]

@pytest.fixture
def negative_list_fixture () :
	return [-2,-4,-8,-10,-12]

@pytest.fixture
def zero_list_fixture () :
 	return [0,0,0,0,0,0,0,0,0,0]

@pytest.fixture
def mix_list_fixture () :
 	return ['a',0,"string",0,0,0,0,0,None]
 # End fixtures region

# AVERAGING
# Basic testing average function
def test_average_above_zero (int_fixture, positive_list_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture) :
	assert algo.average_above_zero(int_fixture) == 2.5
	assert algo.average_above_zero(positive_list_fixture) == 7.2
	
	with pytest.raises(ZeroDivisionError) :
		assert algo.average_above_zero(negative_list_fixture)
		assert algo.average_above_zero(zero_list_fixture)

	with pytest.raises(TypeError) :
		assert algo.average_above_zero(mix_list_fixture)
# END AVERAGING TESTING

# TABLE MAXIMUM VALUE
# Basic max_value testing function
def test_max_value (int_fixture, positive_list_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture) :
	assert algo.max_value(int_fixture) == 4
	assert algo.max_value(positive_list_fixture) == 12
	assert algo.max_value(negative_list_fixture) == -2
	assert algo.max_value(zero_list_fixture) == 0

	with pytest.raises(ValueError) :
		assert algo.max_value(mix_list_fixture)
# END TABLE MAXIMUM TESTING

# TABLE MINIMUM VALUE
# Basic min_value testing function
def test_min_value (int_fixture, positive_list_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture) :
	assert algo.min_value(int_fixture) == -7
	assert algo.min_value(positive_list_fixture) == 2
	assert algo.min_value(negative_list_fixture) == -12
	assert algo.min_value(zero_list_fixture) == 0

	with pytest.raises(TypeError) :
		assert algo.min_value(mix_list_fixture)

# END TABLE MINIMUM TESTING

# REVERSE TABLE
# Basic reverse_table testing function
def test_reverse_table (int_fixture, positive_list_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture) :
	 assert algo.reverse_table(int_fixture) == [-7,4,3,2,1]
	 assert algo.reverse_table(positive_list_fixture) == [12,10,8,4,2]
	 assert algo.reverse_table(negative_list_fixture) == [-12,-10,-8,-4,-2]
	 assert algo.reverse_table(zero_list_fixture) == [0,0,0,0,0,0,0,0,0,0]
	 assert algo.reverse_table(mix_list_fixture) == [None,0,0,0,0,0,"string",0,'a']
# END REVERSE TABLE TESTING

# ROI BBOX
# Basic roi_bbox testing function
# def test_roi_bbox (int_fixture, positive_list_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture) :
	 #assert algo.roi_bbox(int_fixture) == 3
# END ROI BBOX TESTING



