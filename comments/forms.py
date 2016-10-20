from django.forms.models import modelform_factory
from django import forms
from .models import Comment

# CommentForm = modelform_factory(
# 	model = Comment, 
# 	fields=['content'],
# 	widgets = {'content':forms.Textarea}
# )

# class PostCreateForm(forms.ModelForm):
# 	content = forms.CharField(widget=PagedownWidget)
# 	slug = forms.SlugField(initial='auto-filling-do-not-input')
# 	class Meta:
# 		model = Post
# 		fields = ['title', 'slug', 'description', 'content', 'tag']

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea, required=False)
	class Meta:
		model = Comment
		fields = ['content']