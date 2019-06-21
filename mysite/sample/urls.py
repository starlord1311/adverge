from django.conf.urls import include, url
from . import views

# app_name = 'sample'

urlpatterns = [
    url(r'^$', views.add_model , name='index'),
    # url(r'^save/$', views.home,name='home'),
]

# if settings.DEBUG:
# 	urlpatterns += staticfiles_urlpatterns()
# 	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
