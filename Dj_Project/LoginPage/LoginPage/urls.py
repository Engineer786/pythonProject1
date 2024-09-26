"""
URL configuration for LoginPage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tempfile import template

from django.contrib import admin
from django.urls import path, reverse_lazy
from webapp1 import views
# from webapp1.forms import CustomPasswordResetForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # password_reset urls
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='htmlfile/reset_form.html', success_url=reverse_lazy('webapp1:password_reset_done')), name='reset_form'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='htmlfile/reset_done.html'), name='_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='htmlfile/reset_confirm.html', success_url=reverse_lazy('webapp1:password_reset_complete')), name='reset_confirm'),
    path('password_reset_complete_done/', auth_views.PasswordResetCompleteView.as_view(template_name='htmlfile/reset_complete'), name='reset_complete'),
    # others urls
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('home/', views.login),
    path('logout/', views.logout_view),

]
