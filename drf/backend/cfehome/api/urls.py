from api import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_home),               # localhost:8000/api/
    path('api/products',include('products.urls')),   # by doing thi all the path of the project kept in one place   
    path('auth/', obtain_auth_token),
]
