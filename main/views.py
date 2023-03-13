from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import fnmatch
from .models import UserFiles
from django.conf import settings

# Create your views here.
def index(req):
    return render(req, "main/index.html")

def dashboard(req):
    return render(req, "main/dashboard.html")

def edit(req):
    return render(req, "main/edit.html")

def display_video(request,vid=None):
    if vid is None:
        return HttpResponse("No Video")

    #Finding the name of video file with extension, use this if you have different extension of the videos    
    video_name = ""
    for fname in os.listdir(settings.MEDIA_ROOT):
        if fnmatch.fnmatch(fname, vid+".*"): #using pattern to find the video file with given id and any extension
            video_name = fname
            break


    '''
        If you have all the videos of same extension e.g. mp4, then instead of above code, you can just use -

        video_name = vid+".mp4"

    '''

    #getting full url - 
    video_url = settings.MEDIA_URL+video_name

    return render(request, "edit.html", {"url":video_url})

def dropzone_files(request):
	print(request.FILES.get('file'))
	if request.method == "POST":
		image = request.FILES.get('file')
		img = UserFiles.objects.create(image = image)
		
		return HttpResponse({},content_type="application/json")

	return HttpResponse(
		json.dumps({"result": result, "message": message}),
		content_type="application/json"
		)

