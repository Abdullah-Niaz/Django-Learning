from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User

def login_success(sender, request, user, **kwargs):
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user) 
    print(f"Kwargs {kwargs}") 
