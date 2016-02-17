from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Plant(models.Model):
	name = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name