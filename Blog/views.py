from django.shortcuts import render
from django.http import HttpResponse
from.models import Blog
# Create your views here.

def Home(request):
    blog= Blog.objects.all()
    print(blog)
    return render(request,"Blog/Home.html",{"blogs":blog})


def BlogPage(request,id):
    posts=Blog.objects.filter(blog_id=id)
    print(posts)
    value = {"post":posts[0]}
    return render(request,"Blog/BlogPage.html",value)