from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from hitcount.views import HitCountDetailView
from braces.views import LoginRequiredMixin

# Create your views here.
from .models import *
from .forms import PostForm

from comments.views import CommentMixin



class PostLV(ListView):
	model = Post
	paginate_by = 10

class PostDV(CommentMixin ,HitCountDetailView):
	model = Post
	count_hit = True

class PostCV(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	success_url = reverse_lazy('blog:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(PostCV, self).form_valid(form)
		
class PostUV(LoginRequiredMixin, UpdateView):
	model = Post
	form_class = PostForm
	success_url = reverse_lazy('blog:index')

class PostDelV(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('blog:index')	