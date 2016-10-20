from django import forms

from blog.models import Post

class SearchForm(forms.Form):
	search_word = forms.CharField()