from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

# Create your views here.

from braces.views import LoginRequiredMixin
from .models import Comment
from .forms import CommentForm

class CommentMixin(object):
	def get_context_data(self, **kwargs):
		context = super(CommentMixin, self).get_context_data(**kwargs)
		context['comment_form'] = CommentForm
		context['comment_list'] = Comment.objects.filter_by_instance(self.object)
		context['content_type_id'] = ContentType.objects.get_for_model(self.object).id
		context['content_id'] = self.object.id
		return context


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm

	def get_success_url(self):
		cmt = Comment.objects.get(pk=self.kwargs['pk'])
		return cmt.content_object.get_absolute_url()

	def form_valid(self, form):
		ctype_id = self.kwargs['ctype']
		parent_id = self.request.POST.get('parent_id', None)
		form.instance.user = self.request.user
		form.instance.parent = Comment.objects.get(id=int(parent_id)) if parent_id else None
		form.instance.content_type = ContentType.objects.get(id=ctype_id)
		form.instance.object_id = self.kwargs['pk']
		self.object = form.save()
		
		return redirect(self.object.content_object.get_absolute_url())


class CommentDeleteView(LoginRequiredMixin, DeleteView):
	model = Comment
	def get_success_url(self):
		cmt = Comment.objects.get(pk=self.kwargs['pk'])
		return cmt.content_object.get_absolute_url()

