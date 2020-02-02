from django.shortcuts import render
from .models import text_image
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .nerual.text_detection import text_rec

import shutil

@csrf_exempt
def sosi(request):
	if request.method == 'POST':
		a = text_image(image=request.FILES['files'])
		a.save()
		text = text_rec('images/image.jpg')
		shutil.rmtree('images')
		return HttpResponse(text)