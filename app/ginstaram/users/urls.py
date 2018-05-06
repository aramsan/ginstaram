from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('signup', views.signup, name='signup'),
     path('signup/request', views.signupRequest, name='signupRequest'),
     path('picture', views.picture, name='userPicture'),
     path('picture/request', views.pictureRequest, name='userPictureRequest'),
]
