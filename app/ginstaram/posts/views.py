from django.shortcuts import render

def timeline(request):
    return render(request, 'posts/timeline.html')
