
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render_to_response
from django.http import JsonResponse
import json

from .forms import SearchForm
from blog.models import *
from bookmark.models import *


class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)


class HomeView(TemplateView):
	template_name = 'home.html'

class UserCV(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')

class UserCVDone(TemplateView):
	template_name = 'registration/register_done.html'

class SearchView(FormView):
	form_class = SearchForm
	template_name = 'search_result.html'

	def form_valid(self, form):
		kw = self.request.POST['search_word']
		context = {
			'form' : form,
			'search_word' : kw,
			'bookmark_list' : Bookmark.objects.filter(Q(title__icontains=kw)|Q(description__icontains=kw)|Q(url__icontains=kw)),
			'post_list' : Post.objects.filter((Q(title__icontains=kw)|Q(description__icontains=kw)|Q(content__icontains=kw)))
		}
		return render_to_response('search_result.html', context)

def Autocomplete(request):
	if request.is_ajax():
		kw = request.GET['term']
		bookmarks = Bookmark.objects.filter(Q(title__icontains=kw)|Q(description__icontains=kw)|Q(url__icontains=kw))
		blogs = Post.objects.filter((Q(title__icontains=kw)|Q(description__icontains=kw)|Q(content__icontains=kw)))
		ret = []
		for bg in blogs:
			if kw in bg.title:
				ret.append({'title':bg.title, 'kwin':bg.title})
			if kw in bg.description:
				ret.append({'title':bg.title, 'kwin':bg.description})
			if kw in bg.content:
				ret.append({'title':bg.title, 'kwin':bg.content})
		return JsonResponse(ret,content_type="application/json",safe=False)
