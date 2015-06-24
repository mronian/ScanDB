import numpy as np 
import cv2
import os

def nothing(x):
    pass

def getLines(filename):
    print filename
    print "Running RLSA"
    filenamer=filename
    img=cv2.imread(filenamer, cv2.IMREAD_UNCHANGED)
    thresholdh=70
    height, width=img.shape

    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    VAL=0
    #cv2.namedWindow('BW', cv2.WINDOW_AUTOSIZE)
    #cv2.imshow('BW', img)
    #cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
    #cv2.createTrackbar('TH','Original',0, 100,nothing)
    #filenamew="Thresh/Noise2.png"
    #cv2.imwrite(filenamew, doc)
    doc=img.copy()
    h=w=0
    while(h<height):
        c=1
        while(w<width):
            if doc.item(h,w)==VAL:
                if (w-c)<=thresholdh:
                    for i in xrange(c,w):
                        doc.itemset((h, i), VAL)
                c=w
            w=w+1
        if (width-c)<=thresholdh:
            for i in xrange(c,width):
                doc.itemset((h, i), VAL)
        h=h+1 
        w=0
    print "Doc 1 Done for "+ str(thresholdh)
    doc3 = cv2.dilate(doc, element, iterations=2)
    
    contours, hierarchy=cv2.findContours(doc3, 2,cv2.CHAIN_APPROX_SIMPLE)
    tr=0
    # while(1):
    #     tr=0
    for cnt in contours:
        x,y,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(doc3,(x,y),(x+w,y+h),(127),5)
        img2=img[y:y+h, x:x+w]
        filenamew="./Lines/"+ str(tr)+'.jpg'
        cv2.imwrite(filenamew,  img2)
        tr=tr+1
#print tr


if __name__ == "__main__":
    import sys
    getLines(sys.argv[1])