from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('<str:displayUsername>', views.user, name='user'),
     path('signup', views.signup, name='signup'),
     path('signup/request', views.signupRequest, name='signupRequest'),
     path('picture', views.picture, name='userPicture'),
     path('picture/request', views.pictureRequest, name='userPictureRequest'),
     path('login', views.login, name='login'),
     path('login/request', views.loginRequest, name='loginRequest'),
     path('logout', views.logout, name='logout'),
]
