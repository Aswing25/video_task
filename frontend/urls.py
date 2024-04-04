from django.contrib import admin
from django.urls import path

from frontend import views

urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('video_uploadpage/',views.video_uploadpage,name="video_uploadpage"),
    path('save_video/',views.save_video,name="save_video"),
    path('displaypage/',views.displaypage,name='displaypage')


]