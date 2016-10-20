from django.forms.models import modelform_factory
from django import forms
from .models import *

# PostCreateForm = modelform_factory(
# 	model = Post,
# 	fields = ['title', 'image', 'file', 'description','content'],
# 	widgets = {'content': forms.Textarea}
# )



# modelform_factory(model, form, fields, exclude, formfield_callback, widgets, localized_fields, labels, help_texts, error_messages, field_classes)
class PostForm(forms.ModelForm):
	title = forms.CharField(label='제목')
	image = forms.ImageField(label='사진', required=False)
	file = forms.FileField(label='첨부파일', required=False)
	description = forms.CharField(label='설명')
	content = forms.CharField(label='내용작성', widget=forms.Textarea)

	class Meta:
		model = Post
		fields = ['title','image','file','description','content']

