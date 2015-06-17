import numpy as np 
import cv2
import os

def nothing(x):
    pass

def getSegments(filename):
    print filename
    print "Binarisation"

    # command="ocropus-nlbin -n "+filename+" -o book"
    # os.system(command)
    print "Running RLSA"
    filenamer="book/0001.bin.png"
    img=cv2.imread(filenamer, cv2.IMREAD_UNCHANGED)
    thresholdh=70
    thresholdw=47

    height, width=img.shape

    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    VAL=0
    doc=img.copy()
    doc = cv2.dilate(doc, element, iterations=1)
    # doc = cv2.erode(doc, element, iterations=1)

    filenamew="Thresh/Noise2.png"
    cv2.imwrite(filenamew, doc)
    doc2=doc.copy()
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

    while(w<width):
        c=1
        while(h<height):
            if doc2.item(h,w)==VAL:
                if (h-c)<=thresholdw:
                    for i in xrange(c,h):
                        doc2.itemset((i,w), VAL)
                c=h
            h=h+1
        if (height-c)<=thresholdw:
            for i in xrange(c,height):
                doc2.itemset((i,w), VAL)
        w=w+1 
        h=0
    print "Doc 2 Done for "+ str(thresholdh)
    cv2.bitwise_and(doc, doc2, doc)
    doc3 = cv2.dilate(doc, element, iterations=2)
    filenamew="Thresh/Noised.png"
    cv2.imwrite(filenamew, doc3)
    doc3 = cv2.erode(doc3, element, iterations=5)

    filenamew="Thresh/Noisede.png"
    cv2.imwrite(filenamew, doc3)
    contours, hierarchy=cv2.findContours(doc3, 2,cv2.CHAIN_APPROX_SIMPLE)
    tr=0
    area=0
    # cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
    # cv2.createTrackbar('WP','Original',1000,20000,nothing)
    # while(1):
    #     tr=0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>15000:#cv2.getTrackbarPos('WP', 'Original'):
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(doc3,(x,y),(x+w,y+h),(127),5)
            img2=img[y:y+h, x:x+w]
            filenamew="Thresh/Dump1"+ str(tr)+'.png'
            cv2.imwrite(filenamew,  img2)
            tr=tr+1
    print tr
        # es=cv2.waitKey(33)
        # if es==27:
        #     break

    filenamew="Thresh/Bin1"+ str(tr)+'.png'
    cv2.imwrite(filenamew, doc3)


if __name__ == "__main__":
    import sys
    rlsa(sys.argv[1])