from django.conf.urls import patterns, include, url
from django.conf import settings
from OCR import views
from django.conf.urls.static import static


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        #url(r'^user/$', views.user, name='user'),
        ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)