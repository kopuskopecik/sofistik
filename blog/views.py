from django.shortcuts import render

from .models import Blog, Category, Tag




def blog(request):
    categories = Category.objects.all()
    blogs = Blog.objects.filter(active= True)
    
    
    context = {
        "categories": categories,
        "blogs": blogs,
    }    
    return render(request, 'index.html', context)
