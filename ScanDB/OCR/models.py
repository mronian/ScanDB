from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DocUpload(models.Model):
	posted_on = models.DateTimeField(auto_now_add=True, editable=False)
	uploaded_doc = models.ImageField(upload_to='uploads')
	
	def __unicode__(self):
		return self.uploaded_doc
	
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	account_type = models.CharField(max_length=100)
    
	def __unicode__(self):
		return self.user.username