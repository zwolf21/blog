from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class CommentManager(models.Manager):
	def filter_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return super(CommentManager, self).filter(content_type=content_type, object_id=instance.id).filter(parent=None)#.order_by('timestamp')

	# def all(self):
	# 	return super(CommentManager, self).filter(parent=None)#.order_by('timestamp')

	def content_type_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type


class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey("self", null=True, blank=True)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')

	objects = CommentManager()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.user.username

	@property
	def children(self):
		return Comment.objects.filter(parent=self).order_by('timestamp')

	@property
	def is_parent(self):
		return not bool(self.parent)