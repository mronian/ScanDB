import numpy as np 
import cv2
from django.conf import settings

def nothing(x):
    pass

def binarise(filename):
    pathr=settings.BASE_DIR+'/media/uploads/'
    filenamer=pathr+filename
    print filenamer
    doc=cv2.imread(filenamer, cv2.IMREAD_UNCHANGED)
    
    print "Setting the White Point/Black Point for the Image"
    
    #cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
    #cv2.namedWindow('Binary', cv2.WINDOW_AUTOSIZE)
    # cv2.namedWindow('Otsu', cv2.WINDOW_AUTOSIZE)
    gray_doc = cv2.cvtColor(doc, cv2.COLOR_BGR2GRAY)
    #gray_doc=doc
    height, width = gray_doc.shape
    bin_doc = gray_doc.copy()
    pathw=settings.BASE_DIR+'/static/binarised/'
    filenamew=pathw+filename
    cv2.imwrite(filenamew, bin_doc)
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
    #return filenamew

if __name__ == "__main__":
    import sys
    binarise(sys.argv[1])