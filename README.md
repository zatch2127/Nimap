# Nimap
Django REST API for Client &amp; Project Management A Django REST Framework (DRF) API that allows authentication (JWT), client &amp; project management, and user assignments.
How to Run the Code  (Setup Guide)
✅ Step 1: Install Dependencies
Before running the code, ensure you have all the required dependencies installed:



pip install django djangorestframework mysqlclient djangorestframework-simplejwt
If you are using PostgreSQL, install psycopg2:



pip install psycopg2
✅ Step 2: Set Up Django Project
Create a new Django project and app:



django-admin startproject project_management
cd project_management
django-admin startapp api
Then, add api and rest_framework to INSTALLED_APPS in settings.py:

python
Copy
Edit
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'api',
]
✅ Step 3: Configure MySQL in settings.py
Modify settings.py to use MySQL as your database:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',  # MySQL default port
    }
}
If you're using PostgreSQL, replace mysqlclient with psycopg2 and update the ENGINE field:

python

'ENGINE': 'django.db.backends.postgresql',
✅ Step 4: Apply Migrations
Run the following commands to create the necessary database tables:



python manage.py makemigrations
python manage.py migrate
✅ Step 5: Create a Superuser
To create an admin user:
 python manage.py createsuperuser
Then enter the required details:

Username
Password
Email (Optional)
✅ Step 6: Run the Django Server
Start the Django development server:



python manage.py runserver
Your API will be available at:

http://127.0.0.1:8000/api/


