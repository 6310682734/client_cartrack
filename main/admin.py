from django.contrib import admin
from .models import JobTask

# Register your models here.

class JobTaskAdmin(admin.ModelAdmin):
    list_display = ('locationName', 'latitude', 'longtitude', 'linkVideo', 'uid', 'jobId', 'status', 'createdAt', 'updatedAt')
    list_filter = ('status',)
    search_fields = ('locationName', 'uid')

admin.site.register(JobTask, JobTaskAdmin)