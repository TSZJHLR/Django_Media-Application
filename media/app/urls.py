from django.urls import path 
from . import views 

urlpatterns = [
     path('', views.index, name='index'), # home page
     path('delete/<int:file_id>/', views.delete_file, name='delete_file'), # delete file
     path('download/<int:file_id>/', views.download_file, name='download_file'), # download file
]
