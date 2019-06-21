# from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
# from django.template import RequestContext
from django.http import JsonResponse
from .forms import SubscribeForm
from .models import Video


def add_model(request):
	if request.method == "POST" or request.method == "FILES":
		video_description=request.POST['video_description']
		video_duration=request.POST['video_duration']
		video_location=request.POST['video_location']
		video_tags=request.POST['video_tags']
		video_file=request.FILES['video_file']

		Video.objects.create(
			video_description=video_description,
			video_duration=video_duration,
			video_location=video_location,
			video_tags=video_tags,
			video_file=video_file
			)

		return HttpResponseRedirect('/user/create')
	else:
		form = SubscribeForm()
		return render(request, "index.html", {'form': form})

def add_video(self,request):
	template_name= 'templates/index.html'
	form=SubscribeForm()
	posts= Video.objects.all()
	args = {'form' : form, 'posts' : posts }
	return render(request, self.template_name, args)



	# form=SubscribeForm()
	# if request.is_ajax():
	# 	form = SubscribeForm(request.POST ,request.FILES )
	# 	if form.is_valid():
	# 		form.save()
	# 		# instance = form.save(commit=False)
	# 		# instance.user = request.user
	# 		# instance.save()
	# 		# data = {
	# 		# 'message':'form is saved'
	# 		# }
	# 		return JsonResponse(data)
	# 	context = {
	# 	'form':form,
	# 	}
	# 	return HttpResponseRedirect('/')
	# else:
	# 	form = SubscribeForm()
	# 	return render(request, "index.html", {'form': form})
			# # form.save()
			# # data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
			# # context= {'video_file': video_file,
   # #            'form': form
   # #            }
			# # # p = Video()
			# form.video_description=form.cleaned_data['video_description']
			# form.video_duration=form.cleaned_data['video_duration']
			# form.video_location=form.cleaned_data['video_location']    
			# form.video_tags=form.cleaned_data['video_tags']    
			# form.video_file=form.cleaned_data['video_file']
			# form.save()
			# data = {'is_valid': True, 'name': form.video_file.name, 'url': form.video_file.url}
	# 	return HttpResponseRedirect('/')
	# else:
	# 	form = SubscribeForm()
	# 	return render(request, "index.html", {'form': form})

# def get(self, request):
#         photos_list = form.objects.all()
#         return render(self.request, 'templates/index.html', {'photos': photos_list})
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
		