from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

import datetime

def timeline(request):
    post_list = [ 
        {
            'author':{'username':"user1",'picture':"https://placehold.jp/32x32.png"},
            'picture':"https://placehold.jp/800x800.png",
            'like':25,
            'time':"2018-05-10 20:00:00",
            'comment':[
                { 'username':"user1", 'comment':"フォトジェニック"} ,
                { 'username':"user2", 'comment':"面白い"} ,
                { 'username':"user3", 'comment':"かっこいい"} ,
            ],
        },
        {
            'author':{'username':"user1",'picture':"https://placehold.jp/32x32.png"},
            'picture':"https://placehold.jp/800x800.png",
            'like':25,
            'time':"2018-05-09 20:00:00",
            'comment':[
                { 'username':"user1", 'comment':"フォトジェニック"} ,
                { 'username':"user2", 'comment':"面白い"} ,
                { 'username':"user3", 'comment':"かっこいい"} ,
            ],
        },
        {
            'author':{'username':"user1",'picture':"https://placehold.jp/32x32.png"},
            'picture':"https://placehold.jp/800x800.png",
            'like':25,
            'time':"2018-05-08 20:00:00",
            'comment':[
                { 'username':"user1", 'comment':"フォトジェニック"} ,
                { 'username':"user2", 'comment':"面白い"} ,
                { 'username':"user3", 'comment':"かっこいい"} ,
            ],
        },
        {
            'author':{'username':"user1",'picture':"https://placehold.jp/32x32.png"},
            'picture':"https://placehold.jp/800x800.png",
            'like':25,
            'time':"2018-05-07 20:00:00",
            'comment':[
                { 'username':"user1", 'comment':"フォトジェニック"} ,
                { 'username':"user2", 'comment':"面白い"} ,
                { 'username':"user3", 'comment':"かっこいい"} ,
            ],
        },
    ]
    return render(request, 'posts/timeline.html', {'post_list':post_list})

def post(request):
    error =""
    return render(request, 'posts/post.html', {'error': error})

def postRequest(request):
    filename = save_picture_file(request.FILES['picture'])
    creation = Post(picture=filename,text=request.POST.get('text'),like=0);
    creation.save()
    return HttpResponseRedirect(reverse('timeline'))


def save_picture_file(f):
    filename = 'static/profile/' + datetime.datetime.today().strftime('%s') + f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/" + filename
