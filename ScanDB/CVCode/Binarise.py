import numpy as np 
import cv2
from django.conf import settings
import os

def nothing(x):
    pass

def getBinary(filename):
    pathr=settings.BASE_DIR+'/media/uploads/'
    filenamer=pathr+filename
    print filenamer
    doc=cv2.imread(filenamer, cv2.IMREAD_UNCHANGED)
    
    print "Setting the White Point/Black Point for the Image"
    command="ocropus-nlbin -n "+filenamer+" -o ./static/binarised"
    os.system(command)
    command="mv ./static/binarised/0001.bin.png ./static/binarised/"+filename
    os.system(command)
    command="rm ./static/binarised/0001*"
    os.system(command)

if __name__ == "__main__":
    import sys
    binarise(sys.argv[1])