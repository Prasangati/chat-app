from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def mainpage(request):
    return render(request, 'core/front.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('mainpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html',{'form':form})

def custom_logout_view(request):
    logout(request)  # This should clear the session
    return redirect('mainpage')  # Adjust the redirect as needed

def rooms(request):
    return render(request, 'core/rooms.html')
