from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    list_display = ('title', 'description', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title','description','content')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)