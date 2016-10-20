from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from hitcount.views import HitCountDetailView
from braces.views import LoginRequiredMixin

# Create your views here.e
from .models import *
from .forms import BookmarkForm

class BookmarkLV(ListView):
	# model = Bookmark
	context_object_name = 'object_list'
	template_name = 'bookmark/bookmark_list.html'
	paginate_by = 5

	def get_queryset(self):
		return sorted(Bookmark.objects.all(), key=lambda obj:obj.hit_count.hits, reverse=True)


class BookmarkDV(HitCountDetailView):
	model = Bookmark
	count_hit = True


class BookmarkCV(LoginRequiredMixin ,CreateView):
	model = Bookmark
	form_class = BookmarkForm
	success_url = reverse_lazy('bookmark:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(BookmarkCV, self).form_valid(form)


class BookmarkDelV(LoginRequiredMixin, DeleteView):
	model = Bookmark
	success_url = reverse_lazy('bookmark:index')

