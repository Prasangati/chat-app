from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('chat/',views.chats,name='chats'),
    path('chat/randomizer',include('random_chat.urls')),
    path('chat/rooms', include('rooms.urls')),
    path('about/',views.about_enquiry_view,name='about_enquiry'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.custom_logout_view,name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'),name='login'),
]
