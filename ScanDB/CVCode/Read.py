import os
import pytesseract as tess
import Image
from django.conf import settings
import subprocess
import cv2

def getText(filename, numseg):
    for seg in xrange(1, int(numseg)):
        name_gen="./static/segments/"+filename+"_"+str(seg)+".png"
        if cv2.imread(name_gen).shape[0]<600 or cv2.imread(name_gen).shape[1]<600:
            "Image too Small"
            ocr_out=open(settings.BASE_DIR+"/static/OCRfiles/"+filename+"_"+str(seg)+'.txt', 'w+')
            text=tess.image_to_string(Image.open("./static/segments/"+filename+"_"+str(seg)+".png"))
            ocr_out.write(text)
            continue
        command = "ocropus-gpageseg -n --maxcolseps 0 "+name_gen
        subprocess.call(command, shell=True)
        os.system("rm "+settings.BASE_DIR+name_gen.strip('.png')+".pseg.png")
        linelist=len(os.listdir(settings.BASE_DIR+name_gen.strip('.png')))
        ocr_out=open("./static/OCRfiles/"+filename+"_"+str(seg)+".txt", 'w+')
        for i in xrange(1,linelist):
            line="01%04x"%i+".bin.png"
            text=tess.image_to_string(Image.open("./static/segments/"+filename+"_"+str(seg)+"/"+line))+"\n"
            ocr_out.write(text)
        
        os.system("rm -r "+settings.BASE_DIR+"/static/segments/"+filename+"_"+str(seg))
if __name__ == "__main__":
    import sys
    getText(sys.argv[1], sys.argv[2])