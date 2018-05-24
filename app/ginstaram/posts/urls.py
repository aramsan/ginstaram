from django.urls import path

from . import views

urlpatterns = [
     path('', views.timeline, name='timeline'),
     path('post', views.post, name='post'),
     path('post/request', views.postRequest, name='postRequest'),
]
