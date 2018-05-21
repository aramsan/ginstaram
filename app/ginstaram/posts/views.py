from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from users.models import Profile

import datetime

def timeline(request):
    userid = request.session.get('userid')
    post_list = Post.objects.filter(author=userid).order_by('-postid');
    return render(request, 'posts/timeline.html', {'post_list':post_list})

def post(request):
    error =""
    return render(request, 'posts/post.html', {'error': error})

def postRequest(request):
    userid = request.session.get('userid')
    filename = save_picture_file(request.FILES['picture'])
    creation = Post(picture=filename,text=request.POST.get('text'),like=0,author=Profile(id=userid));
    creation.save()
    return HttpResponseRedirect(reverse('timeline'))


def save_picture_file(f):
    filename = 'static/profile/' + datetime.datetime.today().strftime('%s') + f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/" + filename
