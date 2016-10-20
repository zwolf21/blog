from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', PostLV.as_view(), name='index'),
	url(r'^detail/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),
	url(r'^add/$', PostCV.as_view(), name='add'),
	url(r'^update/(?P<slug>[-\w]+)/$', PostUV.as_view(), name='update'),
	url(r'^delete/(?P<slug>[-\w]+)/$', PostDelV.as_view(), name='delete')
]