from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import os
import fnmatch
from .models import UserFiles
from django.conf import settings
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

@login_required(login_url='main:login')
def index(req):
    return render(req, "main/index.html")

#@login_required(login_url='main:login')
def dashboard(req):
    return render(req, "main/dashboard.html")

@login_required(login_url='main:login')
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

#@login_required(login_url='main:login')
def dropzone_files(request):
    url = 'http://localhost:3003/v1/upload'
    if request.method == "POST":
        image = request.FILES['file']
        print(image.content_type, image.name, image.size)
        header = {'Content-Type: multipart/form-data'}
        # img = UserFiles.objects.create(image=image)
        result = requests.post(url, files={"file": image})
        print(result.content)
        return HttpResponse({}, content_type="multipart/form-data")

def call_scheduler(request):
    url = 'http://localhost:8001/'
    if request.method == 'POST':
        r = requests.post('http://localhost:8001/', params=request.POST)
        data = {}

    if r.status_code == 200:
        return HttpResponse('Yay, it worked')
    return HttpResponse('Could not save data')

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
