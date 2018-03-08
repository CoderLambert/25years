from datetime import datetime

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    template = get_template("index.html")
    #now = datetime.now()
    Articals = Artical.objects.all()
    html = template.render(locals())
    return  HttpResponse(html)

def test(request):
    return HttpResponse("test:  success!")

def search(request):
    template = get_template("search_input.html")
    html = template.render(locals())
    return HttpResponse(html)