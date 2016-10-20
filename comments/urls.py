from django.conf.urls import url, include
from .views import *

urlpatterns = [
 	url(r'^add/(?P<ctype>\d+)/(?P<pk>\d+)/$', CommentCreateView.as_view(),  name='add'),
 	url(r'^delete/(?P<pk>\d+)/$', CommentDeleteView.as_view(),  name='delete'),
 	
]

