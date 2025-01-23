from django import forms # import the forms module from django 
from .models import MediaFile # import the MediaFile model from the models module

class MediaFileForm(forms.ModelForm): # create a form class that inherits from the ModelForm class
     class Meta:
          model = MediaFile # set the model attribute to the MediaFile model
          fields = ['file'] # set the fields attribute to the file field of the MediaFile model
