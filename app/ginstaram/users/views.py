from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile

import hashlib

def index(request):
    username = request.session.get('username')
    return render(request, 'users/index.html', {'username': username})

def signup(request):
    error = request.session.get('error')
    if error:   
        del request.session['error']
    return render(request, 'users/signup.html', {'error': error})

def signupRequest(request):
    username = request.POST.get('username')
    rawPassword = request.POST.get('password')
    if Profile.objects.filter(username=username):
        request.session['error'] = 'ID「' + username + '」はすでに使われています'
        return HttpResponseRedirect(reverse('signup'))
    else:            
        password = hashlib.sha256(rawPassword.encode('utf-8')).hexdigest() 
        creation = Profile(username=username, password=password)
        creation.save()
        request.session['username'] = username
        return HttpResponseRedirect(reverse('index'))
