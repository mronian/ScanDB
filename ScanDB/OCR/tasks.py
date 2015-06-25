from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
import sys
CV_CODE_PATH=settings.BASE_DIR+'/CVCode/'
sys.path.insert(0, CV_CODE_PATH)

import Binarise
import Read
import RLSA

@shared_task
def start(filename):
    Binarise.getBinary(filename)
    number_of_segments=RLSA.getSegments(filename.strip('.tif'))
    Read.getText(filename.strip('.tif'), number_of_segments)
    #Shift this to Admin
    #Add Trackbars for Changing Thresholds
    #Field Extraction
    
if __name__ == "__main__":
    import sys
    start(sys.argv[1])