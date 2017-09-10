from django.conf.urls import url
from .views import index

#url for app, add your URL Configuration

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^lab-2/', include(lab_2,namespace='lab-2')),   
]
