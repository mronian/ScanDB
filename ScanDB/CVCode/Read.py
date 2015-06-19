import os

def getText():
    doclist=os.listdir('./static/segments/')
    for doc in doclist:
        command="tesseract ./static/segments/"+doc+" ./static/OCRfiles/"+doc
        os.system(command)
    
    print doclist
    
if __name__ == "__main__":
    import sys
    getText()