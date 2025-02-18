
A Django REST Framework (DRF) API that allows authentication (JWT), client & project management, and user assignments.

## 1. How to Run the Code (Setup Guide)

### ✅ Step 1: Install Dependencies
Before running the code, ensure you have all the required dependencies installed:
```sh
pip install django djangorestframework mysqlclient djangorestframework-simplejwt
```
If you are using PostgreSQL, install psycopg2:
```sh
pip install psycopg2
```

### ✅ Step 2: Set Up Django Project
Create a new Django project and app:
```sh
django-admin startproject project_management
cd project_management
django-admin startapp api
```
Then, add `api` and `rest_framework` to `INSTALLED_APPS` in `settings.py`:
```python
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
```

### ✅ Step 3: Configure MySQL in `settings.py`
Modify `settings.py` to use MySQL as your database:
```python
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
```

### ✅ Step 4: Apply Migrations
Run the following commands to create the necessary database tables:
```sh
python manage.py makemigrations
python manage.py migrate
```

### ✅ Step 5: Create a Superuser
To create an admin user, run:
```sh
python manage.py createsuperuser
```
Then enter the required details:
- Username
- Password
- Email (Optional)

### ✅ Step 6: Run the Django Server
Start the Django development server:
```sh
python manage.py runserver
```
Your API will be available at:
```
http://127.0.0.1:8000/api/
```

## 2. How Did You Run the Machine Test?

The machine test involves running and verifying API endpoints. We do this using **Postman** or **cURL**.

### 🟢 Step 1: Start Django Server
Ensure your Django server is running:
```sh
python manage.py runserver
```
Your API should be available at:
```
http://127.0.0.1:8000/api/
```

### 🟢 Step 2: Obtain Authentication Token (Login Required for All APIs)
#### 1️⃣ Get JWT Token
- **Method:** POST  
- **URL:** `http://127.0.0.1:8000/api/token/`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (JSON):**
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```
- **Response:**
  ```json
  {
      "access": "your_access_token",
      "refresh": "your_refresh_token"
  }
  ```
Copy `access_token` and use it in all API requests.

### 🟢 Step 3: List All Clients
- **Method:** GET  
- **URL:** `http://127.0.0.1:8000/api/clients/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  ```
- **Response Example:**
  ```json
  [
      {
          "id": 1,
          "client_name": "Company A",
          "projects": [],
          "created_at": "2025-02-17T15:02:13Z",
          "created_by": "admin"
      }
  ]
  ```

### 🟢 Step 4: Create a New Client
- **Method:** POST  
- **URL:** `http://127.0.0.1:8000/api/clients/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  Content-Type: application/json
  ```
- **Body (JSON):**
  ```json
  {
      "client_name": "Company C"
  }
  ```
- **Expected Response:**
  ```json
  {
      "id": 7,
      "client_name": "Company C",
      "projects": [],
      "created_at": "2025-02-18T05:27:19Z",
      "created_by": "admin"
  }
  ```

### 🟢 Step 5: Retrieve Client Info (With Assigned Projects)
- **Method:** GET  
- **URL:** `http://127.0.0.1:8000/api/clients/3/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  ```
  - **Expected Response:**
  ```json

{
    "id": 1,
    "client_name": "Company B",
    "projects": [
        {
            "id": 1,
            "project_name": "Project A"
        },
        {
            "id": 2,
            "project_name": "Project A"
        },
        {
            "id": 4,
            "project_name": "Project A"
        },
        {
            "id": 5,
            "project_name": "Project A"
        },
        {
            "id": 6,
            "project_name": "Project A"
        },
        {
            "id": 7,
            "project_name": "Project A"
        }
    ],
    "created_at": "2025-02-17T15:02:13.795352Z",
    "updated_at": "2025-02-18T05:25:39.038304Z",
    "created_by": "zaid"
}
```

### 🟢 Step 6: Update Client Info
- **Method:** PUT  
- **URL:** `http://127.0.0.1:8000/api/clients/2/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  Content-Type: application/json
  ```
- **Body (JSON):**
  ```json
  {
      "client_name": "Company B"
  }
  ```
  - **Expected Response:**
  ```json
  

{
    "id": 2,
    "client_name": "Company B",
    "projects": [],
    "created_at": "2025-02-17T16:23:09.566921Z",
    "updated_at": "2025-02-18T05:29:08.928888Z",
    "created_by": "zaid"

}
  ```

### 🟢 Step 7: Delete a Client
- **Method:** DELETE  
- **URL:** `http://127.0.0.1:8000/api/clients/3/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  ```

### 🟢 Step 8: Create a New Project
- **Method:** POST  
- **URL:** `http://127.0.0.1:8000/api/projects/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  Content-Type: application/json
  ```
- **Body (JSON):**
  ```json
  {
      "project_name": "Project A",
      "client": 7,
      "users": [1]
  }
  ```
  - **Expected Response:**
  ```json

{
    "id": 9,
    "project_name": "Project A",
    "client": 7,
    "users": [
        1
    ],
    "created_at": "2025-02-18T05:31:28.321921Z",
    "created_by": "zaid"
}
```

### 🟢 Step 9: List Projects Assigned to Logged-in User
- **Method:** GET  
- **URL:** `http://127.0.0.1:8000/api/user/projects/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  ```
  - **Expected Response:**
  ```json
 [
    {
        "id": 1,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-17T19:02:36.568657Z",
        "created_by": "zaid"
    },
    {
        "id": 2,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-17T19:11:59.429003Z",
        "created_by": "zaid"
    },
    {
        "id": 4,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-17T19:28:25.691090Z",
        "created_by": "zaid"
    },
    {
        "id": 5,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-17T19:32:18.242247Z",
        "created_by": "zaid"
    },
    {
        "id": 6,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-17T19:40:39.005198Z",
        "created_by": "zaid"
    },
    {
        "id": 7,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-17T19:41:47.906098Z",
        "created_by": "zaid"
    },
    {
        "id": 8,
        "project_name": "Project A",
        "client": 1,
        "users": [
            1
        ],
        "created_at": "2025-02-18T03:51:43.050946Z",
        "created_by": "zaid"
    }
]

  ```

### 🟢 Step 10: Delete a Project
- **Method:** DELETE  
- **URL:** `http://127.0.0.1:8000/api/projects/3/`
- **Headers:**
  ```
  Authorization: Bearer your_access_token
  ```
- **Expected Response:**
  ```
  Status Code: 204 No Content (Project Deleted)
  ```

## 2. DB Design?

![db](https://github.com/user-attachments/assets/d2adad1f-c79f-406c-ba12-becc9e1b98ae)
