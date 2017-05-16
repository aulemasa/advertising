#coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import advertisingForms
from .models import Advertisement

# Create your views here.
def advertisingAdd(request):
    if request.method == 'POST':
        form = advertisingForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))
    else:
        form = advertisingForms()
    return render(request, 'advtapp/form_view.html', {'form': form})


def advertisingList(request):
    advt = Advertisement.objects.order_by('date_pub').filter(active=True)
    advt_counter = Advertisement.objects.order_by('date_pub').filter(active=True).count()
    return render(request, 'advtapp/list_view.html', {'advt': advt, 'advt_counter': advt_counter})
