from django.shortcuts import render

def index(request):
    return render(request, 'users/index.html')

def signup(request):
    return render(request, 'users/signup.html')
