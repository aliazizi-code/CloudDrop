from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('delete/', views.delete_file, name='delete_file'),
    path('download/', views.generate_presigned_url, name='generate_presigned_url')
]
