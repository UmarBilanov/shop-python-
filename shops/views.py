# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


# Create your views here.
def shops(request):
	form = SubscriberForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		print(form)
		print form.cleaned_data

		new_form = form.save()

	return render(request, 'shops/shops.html', locals())


def home(request):
	products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
	return render(request, 'shops/home.html', locals())