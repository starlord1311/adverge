from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Video

def index(request):
    return render(request, 'index.html')

class VideoEntry(CreateView):
    model = Video
    # the fields mentioned below become the entry rows in the generated form
    fields = [ 'video_description','video_duration','video_location','video_tags']
