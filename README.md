
# **Django Rest Framework (DRF)**  

## **INTRODUCTION**  

Django Rest Framework (DRF) is a sub-framework of the Django framework. Django is one of the most popular Python frameworks used in web development. DRF is used to create RESTful APIs that integrate the backend with the frontend. Compared to third-party APIs, DRF gives developers full control over their APIs.  

---

## **Important Requirements in Operating System to Use DRF**  

### **Prerequisites:**  
- **Visual Studio Code (VS Code):** Download and install it from the browser.  
- **Python:** Install the latest version of Python. After installation, check the installed version using:  
  ```bash
  python --version
  ```  
- **Project Setup:**  
  1. Create a new folder on the desktop and name it `drf_project`.  
  2. Open that folder in VS Code.  

- **Setting Up Virtual Environment & Installing Dependencies:**  
  1. Create a `requirements.txt` file and add the following dependencies:  
     ```
     django>=4.0.0
     djangorestframework
     pyyaml
     requests
     django-cors-headers
     ```
  2. Open a new terminal in VS Code and navigate to the project directory.  
  3. Run the following commands:  
     ```bash
     python --version  # Ensure Python is installed
     python -m venv myenv  # Create a virtual environment
     pip freeze  # List the latest versions of installed packages
     pip install -r requirements.txt  # Install required dependencies
     ```

---

## **Step-by-Step Guide to Creating APIs with DRF**  

### **Step #1: Installing Django Framework**  
Django is used for web development. Install Django and create a new Django project using:  
```bash
pip install django
django-admin --version
django-admin startproject projectname  # Create Django project
cd projectname  # Navigate to project folder
python manage.py runserver  # Run the server to check project setup
```

---

### **Step #2: Creating Apps in Django Framework**  
In this project, two apps (`api` and `products`) are created.  

- Apps are sub-projects within a Django project, allowing modular development.  
- Create an app using:  
  ```bash
  python manage.py startapp appname
  ```  
- Register the created app in `settings.py`:  
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'appname',  # Add your app here
  ]
  ```  
- Create `urls.py` inside the app folder and link it in the main `urls.py` file of the project.  

---

### **Step #3: Including DRF in `settings.py`**  
Modify `INSTALLED_APPS` to include DRF:  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'appname',  # Add your app here
]
```

---

### **Step #4: Creating a Python API Client**  
- Create a separate folder named `py_client`.  
- Inside it, create a file `basic.py`.  
- Define the function in `views.py` of the `products` app.  
- Add the URL in `urls.py` of the app.  
- In `basic.py`, define an endpoint variable and set the API URL.  
- Click on the URL to check if the API is working.  

---

### **Step #5: Fetching Data (GET Request)**  
To fetch data from the database, use request methods like `GET` and `POST`.  

---

### **Step #6: Django Model Instance as an API Response**  
To edit or insert values into the model, use:  
```bash
python manage.py shell
```  
- Import the model and create an object.  
- The data is returned in a dictionary (key-value pairs).  

---

### **Step #7: DRF Views and Response**  
Convert API views to DRF views by importing:  
```python
from rest_framework.response import Response
```  
- This response class returns data in JSON format.  

---

### **Step #8: DRF Model Serializers**  
Serializers in DRF work similarly to Django forms.  
- Create a new file `serializers.py` inside the app.  
- Import serializers using:  
  ```python
  from rest_framework import serializers
  ```

---

### **Step #9: Ingesting Data with DRF Views**  

#### **Creating a Model**  
- Define the model in `models.py`.  
- Register the model in `admin.py`:  
  ```python
  admin.site.register(appname)
  ```  
- Run migrations:  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```  

#### **Creating a Serializer**  
- Define a serializer class in `serializers.py` and link it to the model.  

#### **Creating a View**  
- Define a view method in `views.py` using DRF serializers.  
- Use decorators (`POST`, `GET`) for handling requests.  
- Data from `POST` requests is automatically saved in the model.  

#### **Creating a URL**  
- Register the API views in `urls.py` of the app.  

#### **Request Methods:**  
- `POST` – Ingest new data.  
- `GET` – Retrieve all saved data.  

---

### **Step #10: DRF Generic Retrieve APIView**  
- `RetrieveAPIView` fetches a single record using its primary key (ID).  

#### **Key Points:**  
- `RetrieveAPIView` fetches a single record based on ID.  
- It handles lookups, serialization, and 404 errors.  
- Queryset and filtering can be customized.  

#### **Implementation Steps:**  
- Add the API URL in `urls.py` of the app.  
- Create a `details.py` file inside `py_client`.  
- Add the app URL as an endpoint to fetch details of models/products.  

## Step # 11: DRF Generics - `CreateAPIView`  

In Django Rest Framework (DRF), `generics.CreateAPIView` is used to create new records via a `POST` request. It automatically handles serialization and validation.  

### Key Points:  
- `CreateAPIView` handles `POST` requests to create new records.  
- It automatically manages serialization, validation, and saving data.  
- You can extend it with custom validation, authentication, and permissions if needed.  

---

## Step # 12: DRF Generics - `ListAPIView` and `ListCreateAPIView`  

`ListAPIView` is used to retrieve a list of objects, while `ListCreateAPIView` allows both retrieving and creating objects within a single view.  

### **1. `ListAPIView` (Only Fetch Data)**  
- This allows only `GET` requests to list all products.  

### **2. `ListCreateAPIView` (Fetch and Create Data)**  
- This allows both `GET` (fetch all products) and `POST` (add a new product).  

### **3. URL Routing**  

Add the following URL patterns inside `urls.py`:  

```python
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
```

---

## Step # 13: Function-Based Views (FBVs) for Create, Retrieve, or List  

DRF allows using Function-Based Views (FBVs) with the `@api_view` decorator to handle Create, Retrieve, and List operations.  

| Operation           | HTTP Method | Description                              |
|---------------------|------------|------------------------------------------|
| `create_product`   | `POST`      | Create a new product.                   |
| `retrieve_product` | `GET`       | Retrieve a single product by ID.        |
| `list_products`    | `GET`       | List all products.                      |

### **1. Define views in `views.py`**  
- Create view for `POST` (create product).  
- Create view for `GET` (retrieve a single product).  
- Create view for `GET` (list all products).  

### **2. Add URL Routing in `urls.py`**  
Define the URLs for these views in `urls.py`.  

---

## Step # 14: `UpdateAPIView` and `DestroyAPIView`  

In DRF, `UpdateAPIView` is used to update an existing object, while `DestroyAPIView` is used to delete an object. These generic views automatically handle serialization, validation, and HTTP methods.  

### **1. Update a Product**  
Define a built-in view in `views.py` using `ProductUpdateAPIView`.  
- `PUT`: Updates all fields of a product.  
- `PATCH`: Updates only the provided fields.  

### **2. Delete a Product**  
Define a built-in view in `views.py` using `ProductDestroyAPIView`.  

### **3. Add URLs in `urls.py`**  

```python
urlpatterns = [
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update-product'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='delete-product'),
]
```

---

## Step # 15: Using Mixins with `GenericAPIView`  

Mixins provide reusable behaviors that can be combined with Django's generic API views for flexible and modular APIs.  

### **1. List and Create API using Mixins**  
Define a built-in view in `views.py` using `ProductListCreateView`.  

### **2. Retrieve, Update, and Delete API using Mixins**  
Define a built-in view in `views.py` using `ProductRetrieveUpdateDestroyView`.  

### **3. Add URLs in `urls.py`**  

```python
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
```

### **4. Why Use Mixins with `GenericAPIView`?**  

- **Reusability**: Avoid code duplication by mixing functionalities (`list`, `create`, `update`, `delete`).  
- **Flexibility**: Unlike `ListAPIView` or `RetrieveAPIView`, `GenericAPIView` lets you define multiple methods in one class.  
- **Customization**: You can add custom logic inside each method.  

---

## Step # 16: Session Authentication and Permissions  

Django Rest Framework (DRF) provides **Session Authentication** to authenticate users based on Django’s built-in authentication system. It also provides **permissions** to restrict access based on user roles.  

### **1. Enable Session Authentication in `settings.py`**  

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # Enable Session Authentication
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Require authentication by default
    ]
}
```

**Note:** `SessionAuthentication` requires users to be logged in via Django’s login system (`/admin/` or a custom login view).  

### **2. Create a Custom API with Session Authentication**  
Define a built-in view in `views.py` and import `permissions`.  

## **Step #17: User and Group Permissions with Django Model Permissions**  

Django provides a powerful authentication and permission system that allows assigning permissions to individual users or groups. Model-level permissions control who can **create, read, update, or delete** a model’s data.  

### **Assigning Permissions to Users and Groups**  

#### **1. Using Django Admin**  
To manage permissions via Django Admin, follow these steps:  

- First, create a superuser:  
  ```sh
  python manage.py createsuperuser
  ```
- Log into Django Admin at **http://127.0.0.1:8000/admin/**  
- Navigate to **Users & Groups**:  
  - Assign specific permissions to individual users.  
  - Create a new group (e.g., *Product Managers*) and assign model permissions.  

#### **2. Assigning Permissions Programmatically**  
You can also define permissions via code by creating a separate **permissions.py** file inside your app.  

---

## **Step #18: Custom Permissions**  

Django Rest Framework (DRF) provides built-in permission classes, but sometimes you need more control over access. You can create **custom permission classes** to define specific rules.  

### **1. Creating a Custom Permission**  
A custom permission class must inherit from `BasePermission` and override the `has_permission()` or `has_object_permission()` methods.  

- Write the logic for the permissions you need.  
- Define the view for permissions in **views.py** of your app.  

### **2. Checking User Roles (Groups)**  
- Sometimes, you may want to restrict access based on user groups.  
- **Example:** Allow only users in the `"Product Managers"` group.  

### **3. Object-Level Permissions**  
- If you want to control access per object, override `has_object_permission()`.  
- **Example:** Allow users to edit only their own profiles.  

### **4. Combining Multiple Permissions**  
- Combine multiple permissions using `AND`, `OR`, and `NOT` logic.  
- **Example:** Only allow authenticated users **AND** admins.  

### **5. Restrict Access by HTTP Method**  
- Allow only certain HTTP methods.  
- **Example:** Restrict access to **GET requests only**.  

---

## **Step #19: Token Authentication**  

Django Rest Framework (DRF) provides **Token Authentication** to secure APIs. Users receive a **token** after logging in, which they use in API requests instead of sending their username and password each time.  

### **1. Install Required Packages**  
Run the following commands:  
```sh
pip install djangorestframework
pip install djangorestframework-authtoken
```

### **2. Update `settings.py`**  
Add the following to your **INSTALLED_APPS**:  
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',  # Enables Token Authentication
    'yourappname',  # Replace with your actual app name
]
```

### **3. Apply Migrations**  
Run the migration command to create the token table in the database:  
```sh
python manage.py migrate
```

### **4. Configure Token Authentication**  
Update `settings.py` to enable Token Authentication:  
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Enable Token Auth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Require authentication by default
    ]
}
```

---

### **5. Generate Authentication Tokens for Users**  
Each user needs a token to access the API. You can generate tokens manually or automatically when a user registers.  

#### **Option 1: Generate Token Manually**  
Run the following command in the Django shell:  
```sh
python manage.py shell
```
Then, create a token for an existing user (replace `your_user` with an actual user instance):  
```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username="your_user")  # Replace with actual username
token, created = Token.objects.get_or_create(user=user)
print(token.key)
```

#### **Option 2: Generate Token Automatically on User Creation**  
- Create a new file named **signals.py** inside your app folder.  
- Register `signals.py` in **apps.py** of your app.  

Now, a token is **automatically generated** when a new user is created.  

### **6. Add Token Authentication URL in `urls.py`**  
Define an endpoint for users to obtain authentication tokens:  
```python
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
```

Now, users can send their credentials to `/api/token/` and receive a token in response.  

### **Step # 17: User and Group Permissions with Django Model Permission**  

Django provides a powerful user authentication and permission system, allowing you to assign permissions to individual users or groups. Model-level permissions control who can **create, read, update, or delete** a model’s data.  

#### **Assign Permissions to Users and Groups**  

##### **a. Using Django Admin:**  
To allow permissions for the user through a group, first, create a superuser using the following command:  

```bash
python manage.py createsuperuser
```  

1. Log into Django Admin at **http://127.0.0.1:8000/admin/**.  
2. Navigate to **Users & Groups**:  
   - Assign specific permissions to individual users.  
   - Create a new group (e.g., *Product Managers*) and assign model permissions.  

##### **b. Assigning Permissions Programmatically:**  
You can also assign permissions programmatically by writing logic separately in a new file named **`permissions.py`** within your app.  

---

### **Step # 18: Custom Permissions**  

Django Rest Framework (DRF) provides built-in permission classes, but sometimes you need more control over who can access what in your API. You can create custom permission classes to define specific rules.  

#### **1. Creating a Custom Permission**  
A custom permission class must inherit from **`BasePermission`** and override the **`has_permission()`** or **`has_object_permission()`** methods.  

- Write the logic for the permissions you want to add.  
- Define the view for permissions in `views.py` of the app.  

#### **2. Checking User Roles (Groups)**  
- Sometimes, you may want to restrict access based on user groups.  
- **Example:** Allow only users in the *"Product Managers"* group.  

#### **3. Object-Level Permissions**  
- If you want to control access per object, override **`has_object_permission()`**.  
- **Example:** Allow users to edit only their own profiles.  

#### **4. Combining Multiple Permissions**  
- You can combine multiple permissions using **AND, OR, and NOT** logic.  
- **Example:** Allow only *Authenticated Users AND Admins*.  

#### **5. Restrict Access by HTTP Method**  
- You can allow only certain HTTP methods.  
- **Example:** Allow only `GET` requests.  

---

### **Step # 19: Token Authentication**  

Django Rest Framework (DRF) provides **Token Authentication** as a way to secure APIs. With this, users receive a token after logging in, which they use in API requests instead of sending a username and password each time.  

#### **1. Install Required Packages**  

```bash
pip install djangorestframework
pip install djangorestframework-authtoken
```  

#### **2. Add to `INSTALLED_APPS` in `settings.py`**  

```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',  # Enables Token Authentication
    'yourappname',  # Replace with your app name
]
```  

#### **3. Run Migrations**  
```bash
python manage.py migrate
```  

#### **4. Configure Authentication in `settings.py`**  

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Enable Token Auth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Require authentication by default
    ]
}
```  

#### **5. Generate Authentication Tokens for Users**  
Each user needs a token to access the API. You can generate tokens manually or automatically when a user registers.  

##### **Option 1: Generate Token Manually**  
Run the following command in Django Shell:  

```bash
python manage.py shell
```  
Then, write the code to create a token (replace `actual_user` with your user instance).  

##### **Option 2: Generate Token Automatically on User Creation**  
- Create a new file named **`signals.py`** in the app folder.  
- Register this `signals.py` in **`apps.py`** of the app/product folder.  
- Now, a token is automatically generated when a new user is created.  
- Add the URL configuration in `urls.py`.  

---

### **Step # 20: Default DRF Settings (`rest_framework` in `settings.py`)**  

Django Rest Framework (DRF) provides default settings that control authentication, permissions, pagination, throttling, and more. You can configure these settings in your `settings.py` file under the `REST_FRAMEWORK` dictionary.  

#### **1. Add Authentication, Permissions, Pagination, Throttling, and Renderers**  

##### **Throttling**  
Throttling limits the number of requests a client can make to an API within a specified period to prevent abuse and ensure fair usage.  

##### **Types of Throttling in DRF**  

- **`AnonRateThrottle`** – Limits requests for unauthenticated users.  
- **`UserRateThrottle`** – Limits requests for authenticated users.  
- **`ScopedRateThrottle`** – Limits requests based on a specific scope.  
- **Custom Throttling** – You can create your own throttling logic by extending `BaseThrottle`.  

##### **Renderers (`DEFAULT_RENDERER_CLASSES`)**  
Controls the output format.  

---

### **Step # 21: Using Mixins for Permissions**  

DRF provides mixins that allow you to easily manage API permissions. By combining mixins with generic views, we can create reusable permission logic.  

#### **1. Why Use Mixins for Permissions?**  
Using mixins allows us to:  
- Reuse permission logic across multiple views.  
- Keep views clean and maintainable.  
- Customize access control for different user roles.  

#### **2. Creating a Custom Permission Mixin**  
- Create a new file **`mixins.py`** in the app folder.  
- Import the permissions from `permissions.py` and extend them with mixins.  

##### **Types of Mixins**  

| **Mixin**              | **Purpose**                          |
|------------------------|--------------------------------------|
| `IsAdminUserMixin`     | Only admin users can access         |
| `IsAuthenticatedMixin` | Only logged-in users can access     |
| `IsOwnerMixin`         | Only object owners can edit/delete  |
| `ReadOnlyMixin`        | Everyone can read; only authenticated users can edit |  

---

### **Step # 22: ViewSets and Routers**  

In DRF, **ViewSets and Routers** simplify API development by automatically handling CRUD operations and URL routing.  

#### **1. What are ViewSets?**  
A **ViewSet** is a higher-level abstraction that combines multiple views into a single class. Instead of writing separate views for list, retrieve, create, update, and delete, you can use a ViewSet to handle them all.  

#### **2. What are Routers?**  
A **Router** automatically generates URLs for ViewSets, dynamically mapping HTTP methods to ViewSet actions.  

##### **Steps to Implement**  
1. **Define a Model** → Create a model in `models.py`.  
2. **Create a Serializer** → Define `serializers.py`.  
3. **Define a ViewSet** → Implement `views.py`.  
4. **Use a Router for URLs** → Modify `urls.py`.  

👉 Now, you don’t need to manually define URLs for each API action!  

---

### **Step # 23: URLs, Reverse, and Serializers**  

- **URLs:** Define API routes in `urls.py` using `path()` and `re_path()`.  
- **Reverse:** Use `reverse()` to generate URLs dynamically.  
- **Serializers:** Convert Django models into JSON using **ModelSerializer**.  

---

### **Step # 24: ModelSerializer `create()` and `update()` Methods**  

ModelSerializer provides built-in `create()` and `update()` methods to handle object creation and updates.  

#### **1. Default Methods**  
- **`create(validated_data)`** → Creates and saves a new instance.  
- **`update(instance, validated_data)`** → Updates an existing instance.  

#### **2. Customizing Methods**  
- Override `create()` for custom logic (e.g., modifying field values).  
- Override `update()` to enforce additional validation.  

---

### **Step # 25: Custom Validation with Serializers**  

You can perform custom validation in serializers using:  
- **Field-level validation (`validate_<field_name>()`)**  
- **Object-level validation (`validate()`)**  
- **Extra `kwargs` in the Meta class**  
- **Validators argument in fields**  
        
**Step # 26: Request User Data and Customize View Queryset**  

*In Django, you can request user-specific data and customize the queryset based on the logged-in user. This is useful when you want to display only relevant data to each user, such as their own posts, orders, or profile information.*  

### Request User Data in Views  
Django provides the `request.user` object, which represents the currently logged-in user. You can use it in your views to filter querysets.  

**Example:** Fetching User-Specific Data  

### Customizing QuerySet in Class-Based Views  
If you are using Django’s generic class-based views (CBVs), you can override `get_queryset` to return user-specific data.  

**Example:** Restricting Data in `ListView`  

### Customizing QuerySet with Django Rest Framework (DRF)  
If you're working with Django Rest Framework (DRF), you can customize the queryset in a `ViewSet`.  

**Example:** Filtering API Results by User  

### Bonus: Filtering QuerySet in Admin Panel  
If you want to show only relevant data in the Django Admin panel, override `get_queryset` in the admin model.  

---  

**Step # 27: Related Fields and Foreign Key Serializer**  

*When dealing with `ForeignKey` and related fields in Django Rest Framework (DRF), you can serialize relationships in different ways, such as using `PrimaryKeyRelatedField`, `StringRelatedField`, Nested Serializers, or `HyperlinkedRelatedField`.*  

- **Using HyperlinkedRelatedField** *(Hyperlinks Instead of IDs)*  
  This field provides a URL instead of an ID for related objects.  

### Key Points  
- The best approach depends on the use case and API requirements.  
- Use nested serializers when you need full details but be mindful of performance.  
- Use `PrimaryKeyRelatedField` for simple foreign key references to keep responses lightweight.  

---  

**Step # 28: Pagination**  

- For adding Pagination, go to `settings.py`.  
- Add `DEFAULT_PAGINATION_CLASS` in the `REST_FRAMEWORK` section.  
- We can customize the limit of items on each page with the help of pagination classes. There are different types of pagination classes.  

### Types of Pagination  

#### a. LimitOffsetPagination  
Uses `limit` and `offset` query parameters to control the number of records.  

**Query parameters:**  
- `limit`: Number of items per page (e.g., `?limit=10`).  
- `offset`: Number of items to skip (e.g., `?offset=20`).  

#### b. CursorPagination  
**Query parameter:** `cursor`.  

#### c. None (No Pagination)  
If pagination is not required, you can set it to `None` in the settings.  

---  

**Step # 29: A Django-Based Search for Our Product API**  

*You can build a Django-based search API for your product database using Django Rest Framework (DRF). Here's a step-by-step guide.*  

### 1. Setup Your Django Project (If Not Already Done)  
```sh
python manage.py startapp search
```  

### 2. Configure `settings.py`  
Add `'search'` to `INSTALLED_APPS`.  
```python
INSTALLED_APPS = [
    # other apps...
    'rest_framework',
    'products',
]
```  

### 3. Implement the Search API in `views.py`  
Using the following import statements:  
```python
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
```  

### 4. Define URL Routing in `urls.py`  
```python
from django.urls import path
from .views import ProductSearchView

urlpatterns = [
    path('search/', ProductSearchView.as_view(), name='product-search'),
]
```  

### 5. Run the Server  
```sh
python manage.py runserver
```  

---  

**Step # 30: Building Your Search Engine on Algolia**  

- *Algolia provides a third-party API that we integrate into our code.*  
- *Login to Algolia and select Django framework.*  
- *For integration, first install the Algolia package in the Django project.*  
- *Add attributes in `settings.py` and add the prefix of the app/models.*  
- *Create the `index.py` file in each app that we want to connect with Algolia.*  
- *Then use the following import statement to use the Algolia package.*  

```python
from algoliasearch_django import AlgoliaIndex
```  

---  

**Step # 31: Algolia Search Client for Django**  

- Create a new file named `client.py` in the `search` app and implement the code logic using classes/methods.  
- Create a view in `views.py`.  

---  

**Step # 32: Unified Design of Serializers and Indices**  

- *Arrange the view of fields, meaning display only the fields we want to show to the user and hide the fields that should not be shown.*  

---  

**Step # 33: Json web token Authentication with simplejwt**

- Go to Python JWT Client for DRF  web site copy the client side code and create new file in `py_client` 
 named as `jwt.py` and paste all the code in it.

- Add the drf jwt in settings.py in installed apps.
- To use jwt install the package in drf named as;

```python
djangorestframework-simplejwt
```
- To view Token response go to the (jwt.io) and paste your taken.
- The sequences matters when authenticated the drf token in `settings.py`.

**Step # 34: Login via JavaScript Client**

- Create new folder named as `js-client` add two files `index.html` to create login form and `js.client` for
  form functionality using javascript to post form data in database (db).

- To run JavaScript Server;
```python
python -m http.server 8111(port)
```

**Step # 35: Handle Request Blocked by CORS via django-cors-headers**

- *First of all install package django-cors-headers for handle cors request in javascript. Use command;*
```python
pip install -r requirements.txt
```

- *Include corsheaders in Installed_apps in `settings.py` by writting;*
```python
'corsheaders',
```
- *To allow cors headers in js need to add middleware in `settings.py` above the commonMiddleware in 
   Middleware section. Just like that.*
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'corsheaders.middleware.CorsMiddleware', # here add middleware

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
- *To access the cors header from different locations/apis add the urls in allowed hosts in `settings.py`.* 

**Step # 36: Using JWT With JS Client**

- *Add few additions in `client.js`.* 

**Step # 37: Search via Rest Api and JS Client**

