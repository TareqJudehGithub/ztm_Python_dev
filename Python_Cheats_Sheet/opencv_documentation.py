"""
OpenCV

 OpenCV (Open Source Computer Vision) is a great library for 
 computer vision.
"""

""" 
installation
$ pip install opencv-contrib-python

Refer to: https://pypi.org/project/opencv-python/ for installation




"""
import cv2

# read and transfer an image into an array

img = cv2.imread(filename="filepath", flags=0 or 1(default) or -1 )
""" 
flags parameter:

param   color                                   array type

 0:     grayscale                               two-dimintion array
 1:     colored(default)
 -1:    colored with transparency capabilities.
"""
img.ndim    # returns the array type
img.shape   # returns the image original diminsions,a tuple of the number of 
            # rows & columns (height, width), and channels (if the image is color).
        

"""
resizing img using cv2
 Resizing an image means changing the dimensions of it, be it width 
 alone, height alone or changing both of them.

"""

print('Original Dimensions : ',img.shape)

# set new diminsion scale 
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(src=img, dsize=dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
# 0 param means the user will manually closes the images.
cv2.imshow("Resized image", resized)
cv2.waitKey(0)  
cv2.destroyAllWindows()

# See Python_Mega course section 17 for more details and examples on OpenCV.

# face detection using OpenCV
