from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "main/index.html")

def dashboard(req):
    return render(req, "main/dashboard.html")

def file_upload(req):
    if req.method == "POST":
        # my
        return 
    return