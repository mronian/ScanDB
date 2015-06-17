import Binarise
import RLSA
import Read

def start(filename):
    Binarise.getBinary(filename)
    #RLSA.getSegments()
    #Read.getText()
    #Field Extraction
    
if __name__ == "__main__":
    import sys
    start(sys.argv[1])