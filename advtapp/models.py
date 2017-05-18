#coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Advertisement(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    date_pub = models.DateField()
    active = models.BooleanField(verbose_name="Aktywne")
    author = models.ForeignKey(User)

    def __unicode__(self):
        return "{text}".format(text=self.text)

    class Meta:
        ordering = ['date_pub']
