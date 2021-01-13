from django.shortcuts import render

from .models import Blog, Category, Tag
from home.models import Setting




def blog(request):
    setting  = Setting.objects.first()

    categories = Category.objects.all()
    blogs = Blog.objects.filter(active= True)
    
    
    context = {
        "categories": categories,
        "blogs": blogs,
        'setting': setting,

    }    
    return render(request, 'blog.html', context)
