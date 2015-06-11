import numpy as np 
import cv2

def nothing(x):
    pass

doc=cv2.imread('../Datasets/Test1.tif', cv2.IMREAD_UNCHANGED)

print "Setting the White Point/Black Point for the Image"

cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Binary', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('Otsu', cv2.WINDOW_AUTOSIZE)

gray_doc = cv2.cvtColor(doc, cv2.COLOR_BGR2GRAY)
height, width = gray_doc.shape
bin_doc = gray_doc.copy()

# cv2.createTrackbar('WP','Original',0,255,nothing)
# cv2.createTrackbar('BP','Original',255,255,nothing)

# minp= np.amin(gray_doc)
# maxp= np.amax(gray_doc)


# while(1):
# 	wp=cv2.getTrackbarPos('WP', 'Original')
# 	bp=cv2.getTrackbarPos('BP', 'Original')

# 	for h in xrange(height):
# 		for w in xrange(width):
# 			x=gray_doc[h][w]
# 			new_x=x	
# 			if x<wp : new_x=0
# 			bin_doc.itemset((h,w), int(new_x))
# 	# binary_doc = cv2.adaptiveThreshold(gray_doc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
# 	#             cv2.THRESH_BINARY,11,2)
# 	# blur = cv2.GaussianBlur(gray_doc,(5,5),0)
# 	# ret3,otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 	# cv2.imshow('Original', doc)
# 	# cv2.imshow('Binary', bin_doc)

# 	k=cv2.waitKey(33)
# 	if k==27:
# 		break;
	# cv2.imshow('Otsu', otsu)
cv2.destroyAllWindows()