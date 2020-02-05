import cv2
import numpy as np

#read image using opencv
img = cv2.imread('dog.jpg')

#define kernel
box_blur = np.ones((3,3), np.float32) / 9
gaussian_blur = np.array([[1,2,1], [2,4,2], [1,2,1]], np.float32) / 16
edge_detection = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
sharpen = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])

#convolution 
result_sharpen = cv2.filter2D(img, -1, sharpen)
result_blur = cv2.filter2D(img, -1, box_blur)
result_gblur = cv2.filter2D(img, -1, gaussian_blur)
result_edge = cv2.filter2D(img, -1, edge_detection)

#save image
cv2.imwrite('dog_sharpen.jpg', result_sharpen)
cv2.imwrite('dog_blur.jpg', result_blur)
cv2.imwrite('dog_gblur.jpg', result_gblur)
cv2.imwrite('dog_edge.jpg', result_edge)

