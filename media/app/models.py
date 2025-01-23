from django.db import models # creating database models require object relational mapping

# Create your models here.

class MediaFile(models.Model):
     '''
     all the uploaded media file in the application is stored here in MediaFile model 
     with their name, size, type, date_uploaded, category and file
     '''
     CATEGORY_CHOICES = [
          ('Audio', 'Audio'), # `mp3` files
          ('Video', 'Video'), # `mp4` files
          ('Image', 'Image'), # `png`, `jpg`, `jpeg` files
     ]
     
     name = models.CharField(max_length=255) # name of the file
     size = models.PositiveIntegerField() # size of the file in bytes
     type = models.CharField(max_length=10) # type of the file stored as string
     date_uploaded = models.DateTimeField(auto_now_add=True) # date of the file uploaded automatically
     category = models.CharField(max_length=10, choices=CATEGORY_CHOICES) # category of the file, predefined choices for validation
     file = models.FileField(upload_to='uploads/') # store the file in the uploads directory inside media folder

     def __str__(self): # string representation of the model
          return self.name
