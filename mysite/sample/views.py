from __future__ import unicode_literals
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from sample.form import SubscribeForm
from sample.models import Video

def add_model(request):
	if request.method == "POST":
		form = SubscribeForm(request.POST)
		if form.is_valid():
			p = Video()
			p.des=form.cleaned_data['video_description']
			p.dur=form.cleaned_data['video_duration']
			p.location=form.cleaned_data['video_location']    
			p.tags=form.cleaned_data['video_tags']    
			# p.file=form.cleaned_data['video_file']
			p.save()
		return HttpResponseRedirect('/')
	else:
		form = SubscribeForm()
		return render(request, "index.html", {'form': form})
# def add_model(request):
# def index(request):
# 	return render(request, 'index.html')
# # class IndexView(generic.ListView):
# #     # name of the object to be used in the index.html
# #     context_object_name = 'video_list'
# #     template_name = 'sample/templates/index.html'
 
# #     def get_queryset(self):
# #         return Video.objects.all()

# class VideoEntry(CreateView):
# 	model=Video
# 	fields=['video_description','video_duration','video_location','video_tags']	






	# def get(self, request):
	# 	if request.method == 'POST':
	# 		form = SubscribeForm(request.POST)
	# 		if form.is_valid():
	# 			p = Video()
	# 			p.des=form.cleaned_data['video_description']
	# 			p.dur=form.cleaned_data['video_duration']
	# 			p.location=form.cleaned_data['video_location']    
	# 			p.tags=form.cleaned_data['video_tags']    
	# 			p.file=form.cleaned_data['video_file']
	# 			p.save()
	# 			return HttpResponseRedirect('/')
	# 	else:
	# 		form = NewBusinessForm()

		# return render(request, 'templates/index.html', {'form': form})    
  # if a GET (or any other method) we'll create a blank form    
		