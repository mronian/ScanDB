from django import forms
from django.contrib.auth.models import User
from OCR.models import DocUpload, UserProfile

class DocUploadForm(forms.ModelForm):
    uploaded_doc=forms.ImageField()
    class Meta:
        model = DocUpload
        fields = ('uploaded_doc',)
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('account_type',)