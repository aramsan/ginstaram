from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile

import hashlib
import datetime

def index(request):
    username = request.session.get('username')
    profile = Profile.objects.get(username=username)
    profileData = {
    'username': profile.username,
    'picture': profile.picture
    }
    return render(request, 'users/index.html', profileData)

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
        creation = Profile(username=username, password=password, picture='/static/img/dummy.png')
        creation.save()
        request.session['username'] = username
        return HttpResponseRedirect(reverse('index'))

def picture(request):
    return render(request, 'users/picture.html')

def pictureRequest(request):
    username = request.session.get('username')
    filename = save_picture_file(request.FILES['picture'])
    profile = Profile.objects.get(username=username)
    profile.picture = filename
    profile.save()
    return HttpResponseRedirect(reverse('index'))

def save_picture_file(f):
    filename = 'static/picture/' + datetime.datetime.today().strftime('%s') + f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/" + filename
