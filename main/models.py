from django.db import models

# Create your models here.
class UserFiles(models.Model):
	
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(verbose_name="User file", upload_to="")

	def __str__(self):
		return f''
	
class JobTask(models.Model):

	locationName = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longtitude = models.DecimalField(max_digits=9, decimal_places=6)
	linkVideo = models.URLField()
	uid = models.PositiveIntegerField()
	jobId = models.PositiveIntegerField()
	status = models.TextField()
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f''