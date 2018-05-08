from django.shortcuts import render

def timeline(request):
    post_list = [ 
        {
            'author':{'username':"user1",'picture':"https://placehold.jp/32x32.png"},
            'picture':"https://placehold.jp/800x800.png",
            'like':25,
            'time':"2018-05-08T20:00:00Z+09",
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
            'time':"2018-05-08T20:00:00Z+09",
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
            'time':"2018-05-08T20:00:00Z+09",
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
            'time':"2018-05-08T20:00:00Z+09",
            'comment':[
                { 'username':"user1", 'comment':"フォトジェニック"} ,
                { 'username':"user2", 'comment':"面白い"} ,
                { 'username':"user3", 'comment':"かっこいい"} ,
            ],
        },
    ]
    return render(request, 'posts/timeline.html', {'post_list':post_list})
