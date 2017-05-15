#coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible


from django import forms
from .models import Advertisement


class advertisingForms(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title','text','date_pub','author','active')
