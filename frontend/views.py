from django.shortcuts import render,redirect
from frontend import models
from frontend.models import videoDB

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def video_uploadpage(request):
    return render(request,"upload_videos.html")

def save_video(request):
    if request.method =="POST":
        video = request.POST.get('videos')
        names = request.POST.get('name')
        obj = videoDB(videofile=video, Tname=names)
        obj.save()
    return redirect(video_uploadpage)

def displaypage(request):
    videos = videoDB.objects.all()
    return render(request,"display_videopage.html", {"videos" : videos})