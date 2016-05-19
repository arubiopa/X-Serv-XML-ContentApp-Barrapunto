from __future__ import unicode_literals

from django.db import models

class Pages(models.Model):
    name = models.CharField(max_length=32)
    page = models.TextField()
