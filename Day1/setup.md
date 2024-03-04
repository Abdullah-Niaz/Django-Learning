## What we are Covering in Module 1:

- Installing Django
- Creating Django Projects
- Analyaing the Default     
- Django Project Structure


## Django: 
    is python framework that allows us to buil web application and websites

## Install Python Django as a global to create Django Projects

``python -m pip install Django``

Test it by running:   ``django-admin``

## Should I install Django globally?
    If you install Django into the default/global environment then you will only be able to target one version of Django on the computer. This can be a problem if you want to create new websites (using the latest version of Django) while still maintaining websites that rely on older versions.

## Do I need to install Django in every virtual environment?
    ou don't need to create a virtual environment if Django is already installed on your PC. However, it is a good idea to do so to isolate dependencies, manage versions, and test your project.

## Why do we need a virtual environment in Django?
    Creating a virtual environment for your Django application is a best practice that helps to manage dependencies and avoid conflicts with system-level Python installations.