from django.shortcuts import render
import os
import sys
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from OCR.models import DocUpload, UserProfile
from OCR.forms import DocUploadForm, UserForm, UserProfileForm
from tasks import start

def index(request):
    #print os.listdir(settings.BASE_DIR)
    #print settings.BASE_DIR
    ADMIN_T=False
    USER_T=False
    if request.user.is_authenticated()==True :
        profile=UserProfile.objects.get(user=request.user)
        if profile.account_type=='Admin':
            ADMIN_T=True
        elif profile.account_type=='User':
            USER_T=True

    context_dict = {'boldmessage': "ResearchUSA", 'Admin' : ADMIN_T, 'User' : USER_T}
    return render(request, 'OCR/index.html', context_dict)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        profile=UserProfile.objects.get(user=user)
        
        if user:
            if user.is_active:
                login(request, user)
                if profile.account_type=='Admin':
                    return HttpResponseRedirect('/OCR/admin/')
                elif profile.account_type=='User':
                    return HttpResponseRedirect('/OCR/user/')
            else:
                return HttpResponse("Your ResearchUSA account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'OCR/login.html', {})
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/OCR/')
        
def user(request):
    if request.user.is_authenticated()==True :
        if request.method == 'POST':
            print request.POST
            if request.POST.get('Next'):
                doc_approved = request.POST.get('Filename')
                command = "mv "+settings.BASE_DIR+"/static/segments/"+doc_approved+" "+settings.BASE_DIR+"/static/approved/"+doc_approved
                os.system(command)
                print "Next"
            elif request.POST.get('Delete'):
                doc_delete = request.POST.get('Filename')
                command = "mv "+settings.BASE_DIR+"/static/segments/"+doc_delete+" "+settings.BASE_DIR+"/static/needapproval/"+doc_delete
                os.system(command)
                print "Delete"
        doclist=os.listdir(settings.BASE_DIR+'/static/segments')
        if doclist :
            doc=doclist[0]
            ocrdoc='./static/OCRfiles/'+doc.strip('.png')+'.txt'
            OCR_TEXT=open(ocrdoc).read()
            return render(request, 'OCR/user.html', {'url' : str(doc), 'OCR_TEXT' : OCR_TEXT})
        else :
            return render(request, 'OCR/NoFiles.html')
    else :
        return render(request, 'OCR/NotLoggedIn.html', {})

def admin(request):
    if request.user.is_authenticated()==True  :
        profile=UserProfile.objects.get(user=request.user)
        if profile.account_type=='Admin':
            if request.method == 'POST':
                form = DocUploadForm(request.POST, request.FILES)
                if form.is_valid():
                    newdoc = DocUpload(uploaded_doc = request.FILES['uploaded_doc'])
                    newdoc.save()
                    IMAGE_PATH=str(newdoc)
                    start.delay(IMAGE_PATH)
                    return HttpResponseRedirect('/OCR/admin/')
                else:
                    print form.errors
                    return HttpResponse('image upload failed')
            else:
                form=DocUploadForm()
            
            context_dict = {'boldmessage': "ResearchUSA", 'form':form}
            return render(request, 'OCR/admin.html', context_dict)
        else :
            return render(request, 'OCR/unauth.html', {})
    else :
        return render(request, 'OCR/NotLoggedIn.html', {})

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'OCR/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )