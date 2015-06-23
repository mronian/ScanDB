import os
import re
def getRegex():
    dir_files=os.listdir('.')
    
    for f in dir_files:
        text=open(f).read()
    
        mat = re.match(r'[A-Z]*', text)
        if mat :
            print mat.group(0)

if __name__ == "__main__":
    getRegex()