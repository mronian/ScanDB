# ScanDB
OCR Web Interface for Automatic Extraction of Contacts from Directories

##What does it Do?

ScanDB works as a web interface. Install it on a server and you are ready to begin indexing
information from directories and other sources of business details.

##Requirements

1. OpenCV <br>
2. Python 2.7 <br>
3. Django 1.7 <br>
4. Celery 3.1.18<br>
5. Tesseract OCR 3.02 <br>
6. OCROpus <br>
7. PLY (Python Lex-Yacc) 3.6 <br>
8. FuzzyWuzzy
9. Scikit-learn

##Setting it Up

Install the requirements and fire up celery :

    celery -A ScanDB worker --loglevel=info

Once the celery worked is up and running, start the Django server :

    python manage.py runserver

##Users

There are 2 user types.

###Admin

The Admin can add users, upload scanned documents and verify any deleted documents by the users.

###Users

The users can see the scanned image and the extracted information, verify if it is correct and
proceed to click 'Next' or 'Delete' as appropriate. This step is used to train the OCR in correcting
errors after the text is produced by Tesseract.

The process may be completely automated once a sufficient confidence level is acheived.

##How does it Work?

* Auto - Thresholding
* De - Skewing of Scanned Documents
* Binarisation
* Extracting segments of information from scanned pages
* Line Extraction
* OCR by Tesseract
* Correcting OCR with Spell Check, Fuzzy String Matching
* Correcting OCR with learned Neural Network from User corrections
* Regular Expressions for Details like Email, Website, Phone Number etc.
* Analysing Tokens
* Parsing Tokens with a Stochastic Layout Parser
* Layout Parser uses an LR Grammar
* Validating Information
* Showing Information to User
* Learning from Corrections made
