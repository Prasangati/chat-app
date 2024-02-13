from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.custom_logout_view,name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'),name='login'),
]
