from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserFiles(models.Model):
	
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(verbose_name="User file", upload_to="")

	def __str__(self):
		return f''
	
class JobTask(models.Model):

	locationName = models.CharField(max_length=100, null=True ,blank=True)
	latitude = models.DecimalField(max_digits=15, decimal_places=6, null=True ,blank=True)
	longtitude = models.DecimalField(max_digits=15, decimal_places=6, null=True ,blank=True)
	linkVideo = models.URLField(null=True ,blank=True)
	uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True)
	jobId = models.PositiveIntegerField()
	status = models.TextField(null=True ,blank=True)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f''