from django.shortcuts import render

# Create your views here.
def randomizer(request):
    return render(request, 'random_chat/random.html')