import numpy as np 
import cv2
from django.conf import settings
import os

def getBinary(filename):
    pathr=settings.BASE_DIR+'/media/uploads/'
    filenamer=pathr+filename
    print filenamer
    doc=cv2.imread(filenamer, cv2.IMREAD_UNCHANGED)
    
    print "Setting the White Point/Black Point for the Image"
    os.system("mkdir ./static/binarised/"+filename.strip('.tif'))
    command="ocropus-nlbin -n "+filenamer+" -o ./static/binarised/"+filename.strip('.tif')+"/"
    os.system(command)
    command="mv ./static/binarised/"+filename.strip('.tif')+"/0001.bin.png ./static/binarised/"+filename.strip('.tif')+".png"
    os.system(command)
    command="rm -r ./static/binarised/"+filename.strip('.tif')
    os.system(command)

if __name__ == "__main__":
    import sys
    getBinary(sys.argv[1])