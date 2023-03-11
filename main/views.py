from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import UserFiles
# Create your views here.
def index(req):
    return render(req, "main/index.html")

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
