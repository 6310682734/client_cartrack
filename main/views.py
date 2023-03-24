from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import os
import fnmatch
from .models import UserFiles, JobTask
from django.conf import settings
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

#@login_required(login_url='main:login')
def index(req):
    return render(req, "main/index.html")

#@login_required(login_url='main:login')
def dashboard(req):
    return render(req, "main/dashboard.html")

#@login_required(login_url='main:login')
def edit(req):
    return render(req, "main/edit.html")


def display_video(request, vid=None):
    if vid is None:
        return HttpResponse("No Video")

    # Finding the name of video file with extension, use this if you have different extension of the videos
    video_name = ""
    for fname in os.listdir(settings.MEDIA_ROOT):
        # using pattern to find the video file with given id and any extension
        if fnmatch.fnmatch(fname, vid+".*"):
            video_name = fname
            break

    '''
        If you have all the videos of same extension e.g. mp4, then instead of above code, you can just use -

        video_name = vid+".mp4"

    '''

    # getting full url -
    video_url = settings.MEDIA_URL+video_name

    return render(request, "edit.html", {"url": video_url})

@login_required(login_url='main:login')
def dropzone_files(request):
    try:
        user = User.objects.get(id=request.user.id)
    except Exception as e:
        print(e)
    url = 'http://178.128.115.54:3003/v1/upload'
    if request.method == "POST":
        image = request.POST['file']
        print(image)
        #print(image.content_type, image.name, image.size)
        header = {'Content-Type: multipart/form-data'}
        # img = UserFiles.objects.create(image=image)
        result = requests.post(url, files={"file": image})
        json_data = json.loads(result.content)
        print(json_data['data']['filePath'])
        
        if(json_data):
            JobTask.objects.create(
                jobId=json_data['id'], 
                linkVideo=json_data['data']['filePath'], 
                uid=user,
                locationName="default",
                latitude = 0,
                longtitude = 0,
                status="Waiting"
            )
            update_data_task(request, json_data)
            return redirect('main:dashboard')
            #update_data_task(request, json_data)
        # pickup_dict = {}
        # pickup_records=[]

        # for data in result:
        #         print(data)
        # pickup_dict["pickup"]=pickup_records
        return HttpResponse({}, content_type="multipart/form-data")

def recive_hook(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            job = JobTask.objects.get(jobId=json_data['job_id'])
            job.linkVideo=json_data['result']['file_name']
            job.status="SUCCESS"
            job.save()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('Yay, it worked', status=200)
    return HttpResponse('Could not save data')

def update_data_task(request, data_job):
    if request.method == 'POST':
        task_data = JobTask.objects.get(jobId=data_job['id'])
        task_data.latitude = request.POST.get('latitude')
        task_data.longtitude = request.POST.get('longtitude')
        task_data.locationName = request.POST.get('fname')
        task_data.save()
        return redirect('main:dashboard')
    return HttpResponse('Could not update data')


#   Registrations
def RegisterPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')

    context = {"form": form}
    return render(request, 'registration/register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:dashboard')
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('main:login')
