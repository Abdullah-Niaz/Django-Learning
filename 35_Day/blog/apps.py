# myapp/apps.py

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'blog'

    def ready(self): 
        from django.contrib.auth.signals import user_logged_in
        from django.contrib.auth.models import User
        from .signals import login_success

        # Connect the signal in the ready method
        user_logged_in.connect(login_success, sender=User)
