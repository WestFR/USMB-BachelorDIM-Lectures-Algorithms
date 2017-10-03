##
# @author : Francony Steven
# @brief : A file testing
##

import pytest
import numpy
import copy
import S1_algotools as algo

# Fixtures LISTS region
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
# END Fixtures LISTS region

# Fixtures MATRIX region
@pytest.fixture
def mat_fixture() :
	myMat = numpy.zeros([10, 10], dtype = int); 
	myMat[2][2] = 1  
	return myMat

@pytest.fixture
def mat_error_fixture() :
	return numpy.zeros([10, 10], dtype = int);

@pytest.fixture
def mat_little_fixture() :
	return numpy.zeros([5, 5], dtype = int);
 # END fixtures MATRIX region

 # Fixtures RANDOM ARRAY region 
@pytest.fixture
def array_empty() :
 	size = 0
	myMat = numpy.full([size,size],'',dtype='str')
	return myMat

@pytest.fixture
def array_high() :
	size = 2
	myMat = numpy.full([size,size],'',dtype='str')
	return myMat

@pytest.fixture
def array_normal() :
 	size = 6
	myMat = numpy.full([size,size],'',dtype='str')
	return myMat
# END fixtures RANDOM ARRAY region

# Fixtures STRING region
@pytest.fixture
def string_empty() :
	return ""

@pytest.fixture
def string_spaced() :
	return "There is a little string"

@pytest.fixture
def string_unspaced() :
	return "Thereisalittlestring"
# END Fixtures STRING region

# Fixtures LIST region
@pytest.fixture
def list_empty() :
	list = []
	return list

@pytest.fixture
def list_normal() :
	list = range(10)
	return list
# END Fixtures LIST region


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
def test_roi_bbox (mat_fixture, mat_error_fixture, mat_little_fixture) : 
	
	assert algo.roi_bbox(mat_fixture).all() == numpy.array([[2,2],[2,2],[2,2],[2,2]]).all()	

	with pytest.raises(ValueError) :
		assert algo.roi_bbox(mat_error_fixture)

	with pytest.raises(IndexError) :
	 assert algo.roi_bbox(mat_little_fixture)
# END ROI BBOX TESTING


# RANDOM ARRAY FILLING
# Basic random_fill_sparse testing function
def test_random_fill(array_empty, array_high, array_normal):

	# Testing with normal array defined in fixtures
	algo.random_fill_sparse(array_normal,6)

	count = 0
	rows_length = array_normal.shape[0]
	cols_length = array_normal.shape[1]

	
	for row in range(rows_length):
		for col in range(cols_length):
			if array_normal[row][col] == 'X':
				count += 1

	assert count == 6
	# End testing with normal array defined in fixtures

	with pytest.raises(ValueError):
		assert algo.random_fill_sparse(array_empty,5)
		assert algo.random_fill_sparse(array_high,30)
# END RANDOM ARRAY FILLING TESTING

# REMOVE WHITESPACE
# Basic remove_whitespace testing function
def test_remove_whitespace(string_empty, string_unspaced, string_spaced):
	# Empty string testing
	assert algo.remove_whitespace(string_empty) == ""
	# Spaced string testing
	assert algo.remove_whitespace(string_spaced) == copy.deepcopy(string_spaced).replace(" ","")
	# Unspaced string testing
	assert algo.remove_whitespace(string_unspaced) == copy.deepcopy(string_unspaced).replace(" ","")
# END REMOVE WHITESPACE

# RANDOM ITEM SELECTION
# Basic shuffle testing function
def test_shuffle(list_empty, list_normal):
	# Empty list testing
	assert algo.shuffle(list_empty) == []
	# Normal list testing
	assert len(set(algo.shuffle(list_normal)).intersection(copy.deepcopy(list_normal))) == len(algo.shuffle(list_normal))
		#listCopy = copy.deepcopy(list_normal)
		#list_normal = algo.shuffle(list_normal)
		#assert len(set(list_normal).intersection(listCopy)) == len(list_normal)
# END RANDOM ITEM SELECTION TESTING

# SORT SELECTIVE BUBBLE
# Basic sort_selective testing function
def test_sort_selective(list_empty, positive_list_fixture, int_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture):
	# Empty list testing
	assert algo.sort_selective(list_empty) == []
	# Positive values list testing
	assert algo.sort_selective(positive_list_fixture) == sorted(copy.deepcopy(positive_list_fixture))
	# Positive and negative values list testing
	assert algo.sort_selective(int_fixture) == sorted(copy.deepcopy(int_fixture))
	# Negative list testing
	assert algo.sort_selective(negative_list_fixture) == sorted(copy.deepcopy(negative_list_fixture))
	# Zeros list testing
	assert algo.sort_selective(zero_list_fixture) == sorted(copy.deepcopy(zero_list_fixture))
	# Mixing type list testing
	assert algo.sort_selective(mix_list_fixture) == sorted(copy.deepcopy(mix_list_fixture))
# END SORT SELECTIVE BUBBLE

# SORT BUBBLE
# Basic sort_bubble testing function
def test_sort_bubble(list_empty, positive_list_fixture, int_fixture, negative_list_fixture, zero_list_fixture, mix_list_fixture):
	# Empty list testing
	assert algo.sort_bubble(list_empty) == []
	# Positive values list testing
	assert algo.sort_bubble(positive_list_fixture) == sorted(copy.deepcopy(positive_list_fixture))
	# Positive and negative values list testing
	assert algo.sort_bubble(int_fixture) == sorted(copy.deepcopy(int_fixture))
	# Negative list testing
	assert algo.sort_bubble(negative_list_fixture) == sorted(copy.deepcopy(negative_list_fixture))
	# Zeros list testing
	assert algo.sort_bubble(zero_list_fixture) == sorted(copy.deepcopy(zero_list_fixture))
	# Mixing type list testing
	assert algo.sort_bubble(mix_list_fixture) == sorted(copy.deepcopy(mix_list_fixture))
# END SORT BUBBLE