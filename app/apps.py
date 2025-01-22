from django.apps import AppConfig 

'''
to create a custom app configuration class
to used to store metadata for an application.
'''

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
