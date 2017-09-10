from django.conf.urls import url
from lab_2.views import index
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
]
