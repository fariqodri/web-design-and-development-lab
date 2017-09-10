from django.conf.urls import url
from .views import index

#url for app, add your URL Configuration

urlpatterns = [
    url(r'^lab-2/', index, name='index'),  
]
