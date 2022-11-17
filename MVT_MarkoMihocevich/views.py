from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from mvt.models import Familia
from django.shortcuts import render
from MVT_MarkoMihocevich.templates import *



def index(request):
    entries = Familia.objects.all()
    context = {'entries': entries}
    return render(request, 'plantilla.html', context)   
