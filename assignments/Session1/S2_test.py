##
# @author : Francony Steven
# @brief : A file testing
##

import pytest
import S1_algotools

# AVERAGING :
# Basic testing average function
def test_average_above_zero () :
	assert S1_algotools.average_above_zero([1,2,3,4,-7]) == 2.5

test_average_above_zero()
