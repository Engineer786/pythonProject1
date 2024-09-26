from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#from django.urls import reverse
from django.contrib.auth import logout
#from django.shortcuts import redirect
from django.views.decorators.http import require_POST

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           auth_login(request, user)
           return redirect('/home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'htmlfile/signup.html', {'form': form})
# @login_required(login_url='login')
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'htmlfile/login.html', {'form':form})

def login(request):
    return render(request, 'htmlfile/home.html')

# class CustomPasswordResetView(PasswordResetView):
#     form_class = CustomPasswordResetForm
#     template_name = 'htmlfile/reset_form.html'
#
# class CustomPasswordResetDoneView(PasswordResetDoneView):
#      template_name = 'htmlfile/reset_done.html'
#
# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#      template_name = 'htmlfile/reset_confirm.html'
#
# class CustomPasswordResetCompleteView(PasswordResetCompleteView):
#   template_name = 'htmlfile/reset_complete.html'

#@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')
















