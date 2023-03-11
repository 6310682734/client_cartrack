from django.db import models

# Create your models here.
class UserFiles(models.Model):
	
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(verbose_name="User image", upload_to="user_file")

	def __str__(self):
		return f''