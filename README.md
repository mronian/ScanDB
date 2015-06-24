# ScanDB
OCR Web Interface for Automatic Extraction of Contacts from Directories

##What does it Do?

ScanDB works as a web interface. Install it on a server and you are ready to begin indexing
information from directories and other sources of business details.

##Requirements

<Proprietary>

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

<Proprietary>
