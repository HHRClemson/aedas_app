"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from userinfo import views
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userinfo/', include('userinfo.urls')),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^contact/', views.ContactUs, name='contact'),
    url(r'^contactinfo/', views.ContactInfo, name='contactinfo'),
    url(r'^documents/', views.document_list, name='document_list'),
    url(r'^documents_upload/', views.document_upload, name='document_upload'),
    url(r'^add_user/', views.AddUser, name='add_user'),
    url(r'^all_users/', views.AllUsers, name='all_users'),
    url(r'^add_user_form_submission/', views.add_user_form_submission, name='add_user_form_submission'),
    path('pdf_view/<int:id>/', views.Generate, name="pdf_generate"),
    path('map_view/', views.default_map, name="default_map"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
