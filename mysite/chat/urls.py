from django.urls import path
from .views import peer1, peer2, peer
from django.contrib.auth import views as auth
from django.conf import settings
from . import views

urlpatterns = [

    path('', peer, name='peer'),
    path('about/', views.About, name ='about'),
    path('register/', views.register, name ='register'),
    path('login/', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='main.html'), name ='logout'),
    path('contact/', views.contact, name ='contact'),
    path('peer1/', peer1, name='peer1'),
    path('peer2/', peer2, name='peer2'),
]