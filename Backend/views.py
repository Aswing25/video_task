from django.shortcuts import render,redirect
from frontend.models import videoDB
# Create your views here.


def display(request):
    videos = videoDB.objects.all()
    return render(request, "display.html", {"videos": videos})

def edit_page(request,dataid):
    videos  = videoDB.objects.get(id=dataid)
    return render(request,"editpage.html",{'videos':videos})


def update_data(request,dataid):
    if request.method =="POST":
        video = request.POST.get('videos')
        names = request.POST.get('name')
        videoDB.objects.filter(id=dataid).update(videofile = video,Tname= names)
        return redirect(display)


def delete_video(request,dataid):
    data=videoDB.objects.get(id=dataid)
    data.delete()
    return redirect(display)