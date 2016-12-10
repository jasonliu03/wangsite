from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from .models import photo

def index(request):
    photo_list = photo.objects.all()
    context = {'photo_list': photo_list}
    return render(request, 'photo/index.html', context)
