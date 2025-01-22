import os #to work with file paths
from django.http import JsonResponse, HttpResponse #to send json response and file download response
from django.shortcuts import render, get_object_or_404 # to render the html template and get the object from the database
from .models import MediaFile #to work with the model
from .forms import MediaFileForm #to work with the form
from django.conf import settings #to get the settings from the settings.py file

# Define valid file extensions
VALID_EXTENSIONS = {"mp3", "mp4", "jpeg", "png", "gif"}
MIN_FILE_SIZE = 100 * 1024  # 100 KB
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# Create your views here.

def index(request): #index view
     if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest': #check if the request is AJAX and POST 
          form = MediaFileForm(request.POST, request.FILES) # create instance with the POST data and FILES
          if form.is_valid(): # check form validility
               uploaded_file = request.FILES['file'] # get the uploaded file from the form

               # validate file extension
               file_extension = uploaded_file.name.split('.')[-1].lower() # for file extension
               if file_extension not in VALID_EXTENSIONS:   # check validility
                    return JsonResponse({ # JSON response return
                    "status": "error",  # error status
                    "message": f"Invalid file extension: .{file_extension}. Allowed extensions: {', '.join(VALID_EXTENSIONS)}" # error message
                    })
                    
               # validate file size
               if uploaded_file.size < MIN_FILE_SIZE or uploaded_file.size > MAX_FILE_SIZE: # check file size
                    return JsonResponse({ # JSON response return
                         "status": "error",  # error status
                         "message": f"File size must be between 100 KB and 10 MB. Uploaded file size: {uploaded_file.size / 1024:.2f} KB" # error message
                    })
               
               # save the file if valid
               uploaded_file_instance = form.save(commit=False) # save from to database
               uploaded_file_instance.name = uploaded_file.name # set the file name
               uploaded_file_instance.size = uploaded_file.size # set the file size
               uploaded_file_instance.type = uploaded_file.content_type.split('/')[0] # set the file type
               uploaded_file_instance.category = { # set the file category
                    'audio': 'Audio',
                    'video': 'Video',
                    'image': 'Image',
               }.get(uploaded_file_instance.type, 'Other') # get the file category
               uploaded_file_instance.save() # save the file instance
               messages.success(request, "File uploaded successfully!")  # success message
               return JsonResponse({"status": "success"}) # success JSON response
          else:
               messages.error(request, "File upload failed. Please check the file size or type.")  # error message
               return JsonResponse({"status": "error", "errors": form.errors})  # return error JSON response

     files = MediaFile.objects.all() # all the files from the database
     return render(request, "index.html", {"files": files}) # render the html template with the files

def download_file(request, file_id):    # view to download the file
     file = get_object_or_404(MediaFile, id=file_id) # instance of the file
     file_path = file.file.path  # get the file path from the instance
     file_name = os.path.basename(file_path) # get the file name from the file path

     # file reading
     with open(file_path, 'rb') as f: # open the file in binary mode
          response = HttpResponse(f.read(), content_type="application/octet-stream") # create a response with the file content
          response['Content-Disposition'] = f'attachment; filename="{file_name}"' # set the content disposition header to force download
          return response # return the response

def delete_file(request, file_id): # view to delete the file
     if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest': # check if the request is AJAX and POST
          file = get_object_or_404(MediaFile, id=file_id) # get the file instance
          file_path = file.file.path # get the file path from the instance
          file.delete() # delete the file instance
          if os.path.exists(file_path): # check if the file exists
               os.remove(file_path) # remove the file from the file system
          return JsonResponse({"status": "success"}) # success JSON response
     return JsonResponse({"status": "error"}) # error JSON response
