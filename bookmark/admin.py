from django.contrib import admin

# Register your models here.
from .models import *

class BookmarkAdmin(admin.ModelAdmin):
	'''
	   Admin View for Bookmark
    '''
	list_display = ('title', 'description','url',)
	list_filter = ('title',)
	search_fields = ('title','description','url')
	prepopulated_fields = {'description':('title',)}

admin.site.register(Bookmark, BookmarkAdmin)