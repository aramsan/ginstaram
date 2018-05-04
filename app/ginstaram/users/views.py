from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'users/index.html')

def signup(request):
    return render(request, 'users/signup.html')

def signupRequest(request):
    return HttpResponse('post')
