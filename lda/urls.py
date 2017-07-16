from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/topic_over_time', views.topic_over_time, name='topic_over_time'),
    # url(r'^api/fileupload', views.file_upload, name='file_upload'),
]
