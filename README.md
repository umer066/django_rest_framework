 
## Django_Rest_Framework (DRF) :-
        
## INTRODUCTION :-

 "Django rest framework is the sub framework of Django framework. Django 
 framework is the most popular framework of python use in web-development. 
 Django rest framework use to Ceate restful APIs which is use to integrate        
 backend with frontend. We have full control on these rest APIs as compared to 
 third party APIs. "

## Important requirements in Operating system to use DRF:-

 -- Visual studio code (vs code) , download setup from browser and install.
 -- Install Python , try to install latest and updated version of python,        
 after installation write this command to check the installated version.
   -> python --version

 -- Create a new folder on desktop name it drf_project. 
 -- Then open that folder in your vs code.

 -- Now this step is very important, in this we have to create virtual environment 
    and install helping tools(pips) by creating requirements.txt file.

    -- requirements.txt;
       django>=4.0.0
       djangorestframework
       pyyaml
       requests
       django-cors-headers  

 -- Open new terminal in vs code make sure your are using the right directory of 
    the folder, now follow these commands in vs code terminal.

    -> Commands ;
      >> python --version(if show installed version, then go to next step otherwise install python).
      >> python -m venv myenv (use this cmd to create venv).
      >> pip freeze (to list the latest versions of  pips).
      >> pip install -r requirements.txt (to install required pips). 

 -- There are step-by-step instructions to create APIs with Django_rest_framework (drf).  

Step # 01:( Installing Django framework ) :-

 Python provide Django framework for web development. Use following commands to 
 install and create the django framework.

   >> pip install django
   >> django-admin --version
   >> django-admin startproject projectname (to create django project).
   >> cd projectname (to navigate project folder).
   >> python manage.py runserver(runserver to check project has created successfully).


Step # 02:( Creating Apps in Django Framework ) :-

   I have created two apps in this project api and products.

   Apps are the sub-project in the django which we use to create mini project in 
   django main project for that use following commands.

    >> python manage.py startapp appname (create app in main project).
    >> ADD created app in the settings.py file in main django project.       

    INSTALLED_APPS = [
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',

     'appname',  # Add your app here
       ]
 - Create the urls.py in the apps folder and then add the app-url in the main project urls.py .

Step # 03:( Including rest framework in settings.py ) :-

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

Step # 04:( Creating a Python API Client ) :-

 -- Create new folder separetly named as py_client.
 -- Then create new file named as basic.py.
 -- Define function code in view.py of product apps.
 -- Add url in the urls.py of the apps.
 -- In basic.py create variable named as endpoint/apiname/url and create url of api.
 -- Now click on url to check api working properly.

Step # 05:( Echo get Data ) :-

  Fetching the data directly from the database. For fetching data we use request methods like get,post methods.

Step # 06:(Django model instance as an API Response ) :-

  To edit or inserting values in model use commands ;
    >> python manage.py shell

   - Use import command to import model and create object of that models.
   - Returns the data in form of dictionary(key-value pairs).

Step # 07:( Rest Framework View and Response ) :-

  Convert API rest view into django restframework view. For that use imports,

   >> from rest_framework.response import Response

  This response class return the response in the form of the json.

Step # 08:(DRF Model Serializers) :-

  The serializer module in drf has the same working as froms in django. Create new 
  file named as serializers.py in apps. Use import statement to import the 
  serializers.   
  >> from rest_framework import serializers

Step # 09:( Ingest data with DRF views ) :-

  If you want to ingest data (receive and save it) using Django Rest Framework (DRF) views, follow these steps:

  - Create a Model :       
      Create model in the models.py in the app.
      After creating model register it in admin.py use this statement.

       >> admin.site.register(appname)

      Then store your model in database by running migration command.

      >> python manage.py makemigrations
      >> python manage.py migrate
               
   - Create a Serializer :

      'Create serializer class for the model in serializers.py and add model.'

   - Create a view for data :

      'Inside your apps views.py create view method for models and serializers.'
      'Add the request method by using decorates.(POST, GET).'
      'All the data coming from post method automatically saved in the models.'

   - Create a url :

     Create url of the methods views in urls.py of the apps.

   - Request methods :
      > Post method ( to ingest new data).
      > Get method (to retreive all saved data).

Step # 10:( DRF Generics Retrieve APIView ) :-

   In Django Rest Framework (DRF), you can use generics.RetrieveAPIView to fetch a 
   single record from the database using its primary key (ID).

   > Key points:-
      'RetrieveAPIView allows fetching a single record based on its ID.
       It automatically handles lookup, serialization, and 404 handling.
       You can customize queryset and filtering if needed.'

        - Add url routing inside urls.py of your apps.
        - Add the endpoint of api in url.

    > Create details.py in py_client folder and then add the url of the app in the
           form of endpoints. To view the details of the models/products.

Step # 11:( DRF Generics CreateAPIView ) :-

    'In Django Rest Framework (DRF), generics.CreateAPIView is used to create new 
     records via a POST request. It automatically handles serialization and 
     validation.'

    > Key Points:-
     - CreateAPIView handles POST requests to create new records.
     - It automatically manages serialization, validation, and saving data.
     - You can extend it with custom validation, authentication, and permissions if needed.

Step # 12:( DRF Generics listAPIView and listCreateAPIView ) :-

   'In Django Rest Framework (DRF), generics.ListAPIView is used to retrieve a list 
    of objects, while generics.ListCreateAPIView allows both retrieving and creating
    objects with a single view.'

    - ListAPIView (Only Fetch Data);
      'This allows only GET requests to list all products.'

    - ListCreateAPIView (Fetch and Create Data);
      'This allows both GET (fetch all products) and POST (add a new product).'
             
    - Add URL Routing ;

      'Inside the urls.py add url routing like that',

    urlpatterns = [
     path('products/', ProductListAPIView.as_view(), name='product-list'),
     path('products/create/', ProductListCreateAPIView.as_view(), name='product-list-create'),
     ]

Step # 13:( Using function Based views for create, retrieve or list ) :-

   'In Django Rest Framework (DRF), you can use Function-Based Views (FBVs) along 
    with the @api_view decorator to handle Create, Retrieve, and List operations.'

   create_product	        POST	        Create a new product.
   retrieve_product	        GET	        Retrieve a single product by ID.
   list_products	        GET	        List all products.
        
    - define view in views.py for create (post-method).
    - define view in views.py for retrieve (get-method) single product.
    - define view in views.py for list (get-method) all products.

    - Create url :
     'create urls of views in urls.py .'

Step # 14:( Update APIView and Destroy APIView ) :-

   'In Django Rest Framework (DRF), you can use UpdateAPIView to update an existing 
    object and DestroyAPIView to delete an object. These are generic views that 
    automatically handle serialization, validation, and HTTP methods.'

    - Create API View :

    > Update a product ;
                  
    'define built-in view in views.py using (modelnameUpdateAPIView).'

     - PUT: Updates all fields of a product.
     - PATCH: Updates only the provided fields.

    > Delete a Product ;

    'define built-in view in views.py using (modelnameDestroyAPIView).'

     - Deletes a product by its id.

     - Add urls :
      'Add urls of the APIView in the urls.py of the apps.'

      urlpatterns = [
       path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update-product'),
       path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='delete-product'),
       ]
        

Step # 15:( Mixins and a Generics APIView ) :-

   'In Django Rest Framework (DRF), Mixins provide reusable behavior that can be 
    combined with Django's generic API views to create flexible and modular APIs.'

    'The GenericAPIView is a powerful base class that allows you to customize how 
     your API works while still keeping it simple.'

     1. List and Create API using Mixins :
      'define built-in view in views.py using (modelnameListCreateView).'
   
     2. Retrieve, Update, and Delete API using Mixins :
       'define built-in view in views.py using (modelnameRetrieveUpdateDestroyView).''

     - Add urls :
      'Add urls of the APIView in the urls.py of the apps.'

     urlpatterns = [
      path('products/', ProductListCreateView.as_view(), name='product-list-create'),
      path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), (name='product-retrieve-update-destroy'),
     ]

     3. Why Use Mixins with GenericAPIView?

    - Reusability: Mixins allow you to mix functionalities (e.g., list, create, 
      update, delete) without rewriting code.
    - Flexibility: Unlike generic class-based views (ListAPIView, RetrieveAPIView), 
      GenericAPIView lets you define multiple methods in one class.
    - Customization: You can add custom logic inside each method.

Step # 16:( Session authentication and Permissions ) :-

  'Django Rest Framework (DRF) provides Session Authentication to authenticate 
   users based on Django’s built-in authentication system. It also provides 
   permissions to restrict access to APIs based on user roles.'

   Now, enable Session Authentication in settings.py:

   REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.SessionAuthentication',  # Enable Session Authentication
     ],
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',  # Require authentication by default
     ]
     }

    Note: 'SessionAuthentication requires users to be logged in via Django’s login 
      system (/admin/ or a custom login view).'

    > Create a Custom API with Session Authentication :
    'define built-in view in views.py using permissions imports.'

        
Step # 17:( User and Group Permissions with Django Model Permission ) :-

  'Django provides a powerful user authentication and permission system, which 
   allows you to assign permissions to individual users or groups. Model-level 
   permissions control who can create, read, update, or delete a model’s data.'

   > Assign Permissions to Users and Groups :

   a. Using Django Admin;
    ' To allow permissions for the user through group then , first of all 
      we have to create superuser follow this command.'

      >> python manage.py createsuperuser

     - Log into Django Admin at http://127.0.0.1:8000/admin/.

    > Go to Users & Groups:
      - Navigate to Users and assign specific permissions to individual users.
      - Navigate to Groups, create a new group (e.g., Product Managers), and assign model permissions. 

    'You can also assign permissions programmatically by write code logic separetly 
     by creating new file named as permissions.py in app.'

Step # 18:( Custom Permissions ) :-

  'Django Rest Framework (DRF) provides built-in permission classes, but sometimes 
   you need more control over who can access what in your API. You can create 
   custom permission classes to define specific rules.'

    1. Creating a Custom Permission :

     ' A custom permission class must inherit from BasePermission and override the 
       has_permission() or has_object_permission() methods.'

     - Write the code logic according to the permissions which we want to add.
     - Then define the view for permissions in views.py of the apps.

    2. Checking User Roles (Groups) :

     - Sometimes, you may want to restrict access based on user groups.
     - Example: Allow Only Users in "Product Managers" Group.

    3. Object-Level Permissions :

     - If you want to control access per object, override has_object_permission().
     - Example: Allow Users to Edit Only Their Own Profile.

    4. Combining Multiple Permissions :

     - You can combine multiple permissions using AND, OR, and NOT logic.
     - Example: Only Authenticated Users AND Admins.

    5. Restrict Access by HTTP Method :

     - You can allow only certain HTTP methods.
     - Example: Allow Only GET Requests.

        
Step # 19:( Token Authentication ) :-

  ' Django Rest Framework (DRF) provides Token Authentication as a way to secure 
    APIs. With this, users receive a token after logging in, which they use in API 
    requests instead of sending a username and password each time.'

    - First, make sure Django REST Framework is installed:

     >>  pip install djangorestframework
     >>  pip install djangorestframework-authtoken

    - Then, add it to INSTALLED_APPS in settings.py:

     INSTALLED_APPS = [
      'rest_framework',
      'rest_framework.authtoken',      # Enables Token Authentication
      'yourappname',                   # Replace with your app name
      ]

    - Run migrations to create the token table in the database:

     >> python manage.py migrate
   
   -- In settings.py, set the default authentication classes:

    REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES': [
     'rest_framework.authentication.TokenAuthentication',  # Enable Token Auth
     ],
     'DEFAULT_PERMISSION_CLASSES': [
     'rest_framework.permissions.IsAuthenticated',  # Require authentication by default
      ]
   }

    > Generate Authentication Tokens for Users
    ' Each user needs a token to access the API. You can generate tokens manually or 
      automatically when a user registers.'

  - Option 1: Generate Token Manually.
    - Run the following command in Django Shell:
     >> python manage.py shell (then write the code to create token replace  actual user).

  - Option 2: Generate Token Automatically on User Creation.
    - Create new file named as signals.py in app folder.
    - Register this signals.py in apps.py of the app/product folder.

    - Now, a token is automatically generated when a new user is created.
    - Now add the url in urls.py.


Step # 20:( Default DRF Settings [rest_framework in settings.py]) :-

  ' Django Rest Framework (DRF) provides default settings that control 
    authentication, permissions, pagination, throttling, and more. You can 
    configure these settings in your settings.py file under the REST_FRAMEWORK 
    dictionary.'

   -- Go to the settings.py add authentication, permissions, paginations,throttlings and renderers.

    > Throttling :

     'In Django Rest Framework (DRF), throttling is a mechanism that limits the 
      number of requests a client can make to an API within a specified period. 
      It helps prevent abuse, protects resources, and ensures fair usage of the API.'

    -- Types of Throttling in DRF :-

      'DRF provides different types of throttling classes.'

     - AnonRateThrottle – Limits requests for unauthenticated users.
     - UserRateThrottle – Limits requests for authenticated users.
     - ScopedRateThrottle – Limits requests based on a specific scope (useful for 
       API views with different rate limits).
     - Custom Throttling – You can create your own throttling logic by extending BaseThrottle.  

     > Renderers (DEFAULT_RENDERER_CLASSES):-
     'Controls the output format.'

Step # 21:( Using mixins for permissions ) :-

   ' DRF provides mixins that allow you to easily manage API permissions. By combining 
     mixins with generic views, we can create reusable permission logic.'

    1. Why Use Mixins for Permissions?
     Using mixins allows us to:

     - Reuse permission logic across multiple views.
     - Keep views clean and maintainable.
     - Customize access control for different user roles.

    2. Creating a Custom Permission Mixin :

    ' Create new file mixins.py in app folder and then import the permissions from 
      permisssions.py and use permissions by extending them with mixins.'

      You can create a reusable permission mixin that applies permissions to views.
      Example: A Mixin for Admin-Only Access

     > Types of Mixins :-

      Mixin	                            Purpose
    - IsAdminUserMixin	           Only admin users can access
    - IsAuthenticatedMixin	   Only logged-in users can access
    - IsOwnerMixin	           Only object owners can edit/delete
    - ReadOnlyMixin	           Everyone can read,only authenticated user can edit

     > Key Points :-
      - Mixins make permission logic reusable across multiple views.
      - You can combine mixins for more complex permission control.
      - They keep views clean and easy to maintain.

Step # 22:( ViewSets and Routers ) :-   

   ' In Django Rest Framework (DRF), ViewSets and Routers simplify API development by     
     automatically handling CRUD operations and URL routing.'

    1. What are ViewSets?
     'A ViewSet is a higher-level abstraction that combines multiple views into a 
      single class. Instead of writing separate views for list, retrieve, create, 
      update, and delete, you can use a ViewSet to handle them all.'

    🔹 ViewSets save time by reducing redundant code.

    2. What are Routers?
     'A Router automatically generates URLs for ViewSets. Instead of manually defining 
      URLs, routers handle them dynamically.'

    🔹 Routers simplify URL management by mapping HTTP methods to ViewSet actions.

     Step 1: Define a Model ;
       Create a model in models.py.

     Step 2: Create a Serializer ;
       Create a serializers.py file.

     Step 3: Define a ViewSet ;
       Create a views.py file.

     Step 4: Use a Router to Handle URLs ;
       Modify urls.py.

     👉 Now, you don’t need to manually define URLs for each API action!

Step # 23:( Urls, Reverse and Serializers ) :-  

   > URLs:
    - Django uses the urls.py file to map URLs to views.
    - The path() and re_path() functions define routes.
    - In DRF, routers are used for API endpoints.

   > Reverse:
     - reverse() generates URLs dynamically using named routes.
     - In DRF, reverse() works similarly for API endpoints.

   > Serializers:
     - Used in DRF to convert complex data (like Django models) into JSON and vice versa.
     - Example using ModelSerializer.
     - Custom serializer example.

Step # 24:( Model serializer create and update Methods ) :- 

 ' In Django Rest Framework (DRF), ModelSerializer provides built-in create() and
   update() methods that allow you to handle object creation and updates easily.'

   You can override these methods to customize their behavior.

    1. Default create() and update() Methods
      By default, ModelSerializer provides these methods:

     > create(validated_data)
      - Used to create and save a new instance.
      - Calls Model.objects.create(**validated_data).

     > update(instance, validated_data)
      - Used to update an existing instance.
      - Updates instance fields with validated_data and calls instance.save().

    2. Customizing create() Method :

     If you want to customize the creation logic, override create().
     Example: Custom create() Method.

    3. Customizing update() Method :

      If you need to modify how an instance is updated, override update().
      Example: Custom update() Method.

    4. When to Override?

     If you need to add custom logic before saving.
     If you want to modify field values (e.g., formatting text).
     If you need to enforce additional validation.
     If related objects need to be created or updated.

Step # 25:( Custom Validation with Serializers ) :- 

    In Django Rest Framework (DRF), you can perform custom validation in serializers in different ways:

    - Field-level validation (validate_<field_name>()).
    - Object-level validation (validate()).
    - Serializer Meta class with extra_kwargs.
    - Using validators argument in fields.

        
Step # 26:( Request User Data and Customize View Quesryset ) :- 

 ' In Django, you can request user-specific data and customize the queryset
   based on the logged-in user. This is useful when you want to display only 
   relevant data to each user, such as their own posts, orders, or profile information.'

    - Request User Data in Views:

      'Django provides the request.user object, which represents the currently 
       logged-in user. You can use it in your views to filter querysets.'

      Example: Fetching User-Specific Data

    - Customizing QuerySet in Class-Based Views:

     'If you are using Django’s generic class-based views (CBVs), you can override 
      get_queryset to return user-specific data.'

      Example: Restricting Data in ListView

    - Customizing QuerySet with Django Rest Framework (DRF):

      'If you're working with Django Rest Framework (DRF), you can customize the 
       queryset in a ViewSet.'

      Example: Filtering API Results by User

    - Bonus: Filtering QuerySet in Admin Panel:

     'If you want to show only relevant data in the Django Admin panel, override 
     get_queryset in the admin model.'

Step # 27:( Related Fields and foreign key serializer ) :-        

 ' When dealing with ForeignKey and related fields in Django Rest Framework (DRF),
   you can serialize relationships in different ways, such as using 
   PrimaryKeyRelatedField, StringRelatedField, Nested Serializers, or 
   HyperlinkedRelatedField.'

    - Using HyperlinkedRelatedField (Hyperlinks Instead of IDs)
    - This field provides a URL instead of an ID for related objects.

   > Key Points :- 
    - The best approach depends on the use case and API requirements.
    - Use nested serializers when you need full details but be mindful of performance.
    - Use PrimaryKeyRelatedField for simple foreign key references to keep responses lightweight.