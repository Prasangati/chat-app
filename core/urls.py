from django.contrib.auth.views import  LoginView
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('start-google-login/', views.start_google_login, name='start-google-login'),
    path('social-auth/', include('social_django.urls', namespace='social')),  # Include social auth URLs
]