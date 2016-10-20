"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCV.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCVDone.as_view(), name='register_done'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^search/autocomplete/$', Autocomplete, name='autocomplete'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', 'bookmark')),
    url(r'^blog/', include('blog.urls', 'blog')),
    url(r'^comments/', include('comments.urls', 'comments'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
