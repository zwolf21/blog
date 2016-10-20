from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from hitcount.models import HitCountMixin


# Create your models here.

class Bookmark(models.Model, HitCountMixin):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=512)
	url = models.URLField('uri', unique=True)
	last_visit_date = models.DateTimeField(auto_now_add=True)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)
	# visit_count = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('bookmark:detail', args=(self.id,))


