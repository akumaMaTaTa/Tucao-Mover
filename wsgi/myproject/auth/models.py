from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50, unique = True)
	password = models.CharField(max_length=50)