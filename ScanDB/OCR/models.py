from django.db import models
import os
from django.contrib.auth.models import User
# Create your models here.


def update_filename(instance, filename):
    path = "uploads/"
    idx=str(DocUpload.objects.all().aggregate(models.Max('id'))['id__max'])
    if idx=='None':
	idx='0'
    return path+idx+'.tif'

class DocUpload(models.Model):
	
	posted_on = models.DateTimeField(auto_now_add=True, editable=False)
	uploaded_doc = models.ImageField(upload_to=update_filename)
	
	
	def __unicode__(self):
		return os.path.basename(self.uploaded_doc.name)

class UserProfile(models.Model):
	Admin_type = "Admin"
	User_type= "User"
	
	User_Account_Types= ((Admin_type, 'Admin'), (User_type , 'User'))
	user = models.OneToOneField(User)
	account_type = models.CharField(max_length=100, choices=User_Account_Types, default=User_type)
    
	def __unicode__(self):
		return self.user.username
	
