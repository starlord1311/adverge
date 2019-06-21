# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Video(models.Model):
	video_description = models.CharField(max_length=100)
	video_duration = models.CharField(max_length=100)
	video_location = models.CharField(max_length=100)
	video_tags = models.CharField(max_length=100)
	video_file = models.FileField(upload_to='image/')
    # on submit click on the product entry page, it redirects to the url below. 
	def __str__(self):   # __unicode__ on Python 2
		return self.video_description
