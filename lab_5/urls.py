from django.conf.urls import url
from .views import index, add_todo, delete

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_todo', add_todo, name='add_todo'),
	url(r'^delete/(?P<id>\w{0,50})/$', delete, name='delete')
]
