from django.shortcuts import render
from newPosts.models import newPost

def home(request):
    blogPost = newPost.objects.all().order_by('-id')[:3]
    data = {
        'blogPost' : blogPost
    }
    return render(request, 'index.html',data)

def blog(request):
    blogPost = newPost.objects.all().order_by('-id')
    data = {
        'blogPost' : blogPost
    }
    return render(request, 'blog.html',data)

def singlePost(request,title_slug):
    blogPost = newPost.objects.get(titleSlug=title_slug)
    data = {
        'blogPost' : blogPost
    }
    return render(request, 'singlePost.html',data)