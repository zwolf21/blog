from django import forms
from .models import *

class BookmarkForm(forms.ModelForm):
	title = forms.CharField(label='제목')
	description = forms.CharField(label='설명', required=False)
	url = forms.URLField(label='URL')
	class Meta:
		model = Bookmark
		fields = ['title','description','url']

 
