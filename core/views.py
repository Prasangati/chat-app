from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def mainpage(request):
    return render(request, 'core/front.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainpage')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('mainpage')

def start_google_login(request):
    return redirect('social:begin', backend='google-oauth2')
