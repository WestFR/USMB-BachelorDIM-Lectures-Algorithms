##
# @author : Francony Steven
# @brief : Images process tools script
##

import cv2 as cv # Impossible to install cv2 on my Mac. I can't test this file.. Sorry ! (edit on 31/09/2017)
import numpy as np 


# Add images
imgGrey = cv.imread("leopard.png",0)
imgBackground = cv.imread("elephant.png",1)
imgThresholded = cv.imread("bird.png",2)


# Display matrix
print("Gray levels on image = "+ str(imgGrey.shape))
print("Background image = "+ str(imgBackground.shape))

# Display images
cv.imshow("Gray image", imgGrey)
cv.imshow("Background image", imgBackground)


#
#	Function inverse the color of an image MANUALLY
#
def invert_colors_manual(input_img):

	imgInversed = np.zeros(input_img.shape, dtype=np.uint8)

	if len(input_img.shape) == 3:
		for x in xrange(input_img.shape[0]):
			for y in xrange(input_img.shape[1]):
				for z in xrange(input_img.shape[2]):
					imgInversed[x,y,z] = 255 - input_img[x,y,z]

	elif len(input_img.shape) == 2:
		for x in xrange(input_img.shape[0]):
				for y in xrange(input_img.shape[1]):
					imgInversed[x,y] = 255 - input_img[x,y]

	return imgInversed

#
#	Function inverse the color of an image with NUMPY
#
def invert_colors_numpy(input_img):
	return (255 - input_img)

#
#	Function inverse the color of an with OPENCV
#
def invert_colors_opencv(input_img):
	return cv.bitwise_not(input_img)

#
#	Function threshold an image with NUMPY
#
def threshold_image_numpy(input_img):
	return (input_img > 127).astype(np.uint8) * 255


imgThreshold = threshold_image_numpy(imgThresholded)

cv.imshow("image", imgThreshold);
cv.waitKey(0)