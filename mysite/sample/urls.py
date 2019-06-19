from django.conf.urls import include, url

from django.contrib.auth.views import login

from django.contrib import admin
from sample import views

app_name = 'sample'

urlpatterns = [
    url(r'^$', views.add_model , name='index'),]
