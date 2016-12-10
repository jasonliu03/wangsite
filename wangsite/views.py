from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def home(request):
    #return HttpResponse("<h1>hello world</h1>")
    return render_to_response("index.html")
