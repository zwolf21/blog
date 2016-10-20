from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', BookmarkLV.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
	url(r'^add/$', BookmarkCV.as_view(), name='add'),
	url(r'^delete/(?P<pk>\d+)/$', BookmarkDelV.as_view(), name='delete'),

]
