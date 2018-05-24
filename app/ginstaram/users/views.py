from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile
from posts.models import Post

import hashlib
import datetime

def index(request):
    username = request.session.get('username')
    if username:
        profile = Profile.objects.get(username=username)
        post_list = Post.objects.filter(author=profile.id).order_by('-postid');
        profileData = {
        'is_mypage': True,
        'username': profile.username,
        'picture': profile.picture,
        'post_list': post_list
        }
        return render(request, 'users/index.html', profileData)
    else:
        return HttpResponseRedirect(reverse('login'))

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
        request.session['userid'] = creation.id
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

def login(request):
    if request.session.get('username'):
        return HttpResponseRedirect(reverse('logout'))
    error = request.session.get('error')
    if error:   
        del request.session['error']
    return render(request, 'users/login.html', {'error':error} )

def loginRequest(request):
    username = request.POST.get('username')
    rawPassword = request.POST.get('password')
    password = hashlib.sha256(rawPassword.encode('utf-8')).hexdigest()
    profile = Profile.objects.filter(username=username, password=password).first()
    if profile:
        request.session['username'] = profile.username
        request.session['userid'] = profile.id
        return HttpResponseRedirect(reverse('timeline'))
    else:
        request.session['error'] = 'IDとパスワードが一致しません'
        return HttpResponseRedirect(reverse('login'))

def logout(request):
    if request.session.get('username'):
        del request.session['username']
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponseRedirect(reverse('index'))

def save_picture_file(f):
    filename = 'static/picture/' + datetime.datetime.today().strftime('%s') + f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/" + filename

def user(request, displayUsername):
    profile = Profile.objects.get(username=displayUsername)
    post_list = Post.objects.filter(author=profile.id).order_by('-postid');
    profileData = {
    'username': profile.username,
    'picture': profile.picture,
    'post_list': post_list
    }
    return render(request, 'users/index.html', profileData)
