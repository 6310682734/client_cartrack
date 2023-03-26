from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:jobId>', views.edit, name='edit'),
    path('dropzone-files', views.dropzone_files, name="dropzone-files"),
    path('webhook/task', csrf_exempt(views.recive_hook), name="webhook-task"),
    path('update-data-task', views.update_data_task, name="update-data-task"),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)