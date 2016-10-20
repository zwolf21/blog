from os.path import basename
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from hitcount.models import HitCountMixin

class Post(models.Model, HitCountMixin):
	user = models.ForeignKey(User)
	title = models.CharField('제목', max_length=50)
	slug = models.SlugField('SLUG', unique=True, allow_unicode=True)
	description = models.CharField('설명', max_length=250, blank=True)
	content = models.TextField('내용')
	image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
	file = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
	create_date = models.DateTimeField('만든날짜', auto_now_add=True)
	modify_date = models.DateTimeField('수정한 날짜', auto_now=True)
	
	class Meta:
		ordering = ['-modify_date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', args=(self.slug,))

	def get_previous_post(self):
		return self.get_previous_by_modify_date()

	def get_next_post(self):
		return self.get_next_by_modify_date()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title, allow_unicode=True)
		return super(Post, self).save(*args, **kwargs)

	def get_file_name(self):
		return basename(self.file.name)
