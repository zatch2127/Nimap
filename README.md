# Nimap
Django REST API for Client &amp; Project Management A Django REST Framework (DRF) API that allows authentication (JWT), client &amp; project management, and user assignments.
1.How to Run the Code  (Setup Guide)
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
        'PORT': '3306', 
    }
}

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

2. How Did You Run the Machine Test?

The machine test involves running and verifying API endpoints. We do this using **Postman** or **cURL**.

### **🟢 Step 1: Start Django Server**
First, ensure your Django server is running:
Terminal 
python manage.py runserver
Your API should be available at:

http://127.0.0.1:8000/api/

Step 2: Obtain Authentication Token (Login Required for All APIs)
Since the API requires authentication, you need a JWT token.

1️⃣ Get JWT Token
Method: POST
URL:
ruby

http://127.0.0.1:8000/api/token/
Headers:
pgsql

Content-Type: application/json
Body (JSON):
json

{
    "username": "your_username",
    "password": "your_password"
}
Response:
json

{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
Copy access_token and use it in all API requests.

🟢 Step 3: List All Clients
Method: GET
URL:
ruby

http://127.0.0.1:8000/api/clients/
Headers:
makefile

Authorization: Bearer your_access_token
Response Example:
json

[
    {
        "id": 1,
        "client_name": "Nimap",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Rohit"
    },
    {
        "id": 2,
        "client_name": "Infotech",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Rohit"
    }
]
🟢 Step 4: Create a New Client
Method: POST
URL:
ruby

http://127.0.0.1:8000/api/clients/
Headers:
pgsql

Authorization: Bearer your_access_token
Content-Type: application/json
Body (JSON):
json

{
    "client_name": "Company A"
}
Expected Response:
json

{
    "id": 3,
    "client_name": "Company A",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Your Username"
}
🟢 Step 5: Retrieve Client Info (With Assigned Projects)
Method: GET
URL:
ruby

http://127.0.0.1:8000/api/clients/3/
Headers:
makefile

Authorization: Bearer your_access_token
Expected Response:
json

{
    "id": 3,
    "client_name": "Infotech",
    "projects": [
        {
            "id": 1,
            "name": "Project A"
        }
    ],
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2019-12-24T11:03:55.931739+05:30"
}
🟢 Step 6: Update Client Info
Method: PUT
URL:
http://127.0.0.1:8000/api/clients/3/
Headers:
pgsql

Authorization: Bearer your_access_token
Content-Type: application/json
Body (JSON):
json

{
    "client_name": "Company B"
}
Expected Response:
json

{
    "id": 3,
    "client_name": "Company B",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Your Username",
    "updated_at": "2019-12-24T11:03:55.931739+05:30"
}
🟢 Step 7: Delete a Client
Method: DELETE
URL:
ruby

http://127.0.0.1:8000/api/clients/3/
Headers:
makefile

Authorization: Bearer your_access_token
Expected Response:
yaml

Status Code: 204 No Content (Client Deleted)
🟢 Step 8: Create a New Project
Method: POST
URL:
ruby

http://127.0.0.1:8000/api/projects/
Headers:
pgsql

Authorization: Bearer your_access_token
Content-Type: application/json
Body (JSON):
json

{
    "project_name": "Project A",
    "client_id": 1,
    "users": [1]
}
Expected Response:
json

{
    "id": 3,
    "project_name": "Project A",
    "client": "Nimap",
    "users": [
        {
            "id": 1,
            "name": "Rohit"
        }
    ],
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Ganesh"
}
🟢 Step 9: List Projects Assigned to Logged-in User
Method: GET
URL:
arduino

http://127.0.0.1:8000/api/user/projects/
Headers:
makefile

Authorization: Bearer your_access_token
Expected Response:
json

[
    {
        "id": 1,
        "project_name": "Project A",
        "client_name": "Client A",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Ganesh"
    },
    {
        "id": 2,
        "project_name": "Project B",
        "client_name": "Client A",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Ganesh"
    }
]
🟢 Step 10: Delete a Project
Method: DELETE
URL:
http://127.0.0.1:8000/api/projects/3/
Headers:
makefile

Authorization: Bearer your_access_token
Expected Response:
yaml

Status Code: 204 No Content (Project Deleted)
