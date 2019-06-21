from django import forms
from django.forms import ModelForm
from sample.models import Video

class SubscribeForm(forms.ModelForm):
	class Meta:
		model= Video
		fields = ['video_description','video_duration','video_location','video_tags','video_file']	
  # video_description = forms.CharField(label='Description', max_length=100)
  # video_duration = forms.CharField(label='Duration', max_length=120)
  # video_location = forms.CharField(label='Location', max_length=100)
  # video_tags = forms.CharField(label='Tags', max_length=120)
  # video_file = forms.fileField(label='Upload',upload_to ='/Photos')