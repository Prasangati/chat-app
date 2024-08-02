from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SignUpForm, EnquiryForm

# Create your views here.
def mainpage(request):
    return render(request, 'core/front.html')


def enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f'Enquiry from {name}',
                message,
                email,
                ['prasangahere@gmail.com'],  # Replace with your email
            )

            return redirect('mainpage')
    else:
        form = EnquiryForm()
    return render(request, 'core/about.html', {'form': form})


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
