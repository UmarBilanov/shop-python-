# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=128)

	def __str__(self):
		return "Пользователь %s %s" % (self.name, self.email,)

	class Meta:
		verbose_name = 'MySubscriber'
        verbose_name_plural = 'MySubscribers'