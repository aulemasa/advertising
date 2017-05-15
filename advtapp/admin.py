#coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

from django.contrib import admin
from .models import Advertisement
# Register your models here.
admin.site.register(Advertisement)
