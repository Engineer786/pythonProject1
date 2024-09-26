"""Dj_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('read/<int:pk>', views.read_data),
    path('readdata/', views.read_data),
    path('create/', views.read_data),
    path('read/<int:pk>', views.employee_details),
    #path('login/', obtain_auth_token, name='login'),
    path('update/<int:pk>', views.employee_details),
    path('delete/<int:pk>', views.employee_details),
]
