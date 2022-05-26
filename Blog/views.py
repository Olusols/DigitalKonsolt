from django.shortcuts import render

# Create your views here.
from .models import Blog, Comment

def blog(request):
    blog = Blog.objects.all()
    
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog.html')

