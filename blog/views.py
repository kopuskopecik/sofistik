from django.shortcuts import render, get_object_or_404

from .models import Blog, Category, Tag
from home.models import Setting, Service




def blog(request):
    setting  = Setting.objects.first()
    services = Service.objects.filter(service_or_not=True, active = True, software = False)
    solutions = Service.objects.filter(service_or_not=False, active = True, software = False)
    #setting  = Setting.objects.first()

    categories = Category.objects.all()
    blogs = Blog.objects.filter(active= True)
    tags = Tag.objects.all()
    recent_blogs = Blog.objects.all()[0:5]
    
    
    context = {
        "categories": categories,
        "blogs": blogs,
        "recent_blogs": recent_blogs,
        "tags": tags,
        'setting': setting,
        'services': services,
        'solutions': solutions,

    }    
    return render(request, 'blog.html', context)

def detail(request, slug):
    blog = get_object_or_404(Blog, slug = slug, active = True)

    setting  = Setting.objects.first()
    services = Service.objects.filter(service_or_not=True, active = True, software = False)
    solutions = Service.objects.filter(service_or_not=False, active = True, software = False)
    categories = Category.objects.all()

    
    
    context = {
        "blog": blog,
        'categories': categories,
        'setting': setting,
        'services': services,
        'solutions': solutions
    }
    return render(request, 'blog-single.html', context)


def categories_detail(request, slug):
    category = get_object_or_404(Category, slug = slug)

    blogs = Blog.objects.filter(active= True, category= category)
    services = Service.objects.filter(service_or_not=True, active = True, software = False)
    solutions = Service.objects.filter(service_or_not=False, active = True, software = False)
    setting  = Setting.objects.first()
    

    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_blogs = Blog.objects.all()[0:5]
    
    
    context = {
        "categories": categories,
        "blogs": blogs,
        "recent_blogs": recent_blogs,
        "tags": tags,
        'setting': setting,
        'services': services,
        'solutions': solutions,

    }    

    return render(request, 'blog.html', context)


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug = slug)
    blogs = tag.blog_set.all()
    
    services = Service.objects.filter(service_or_not=True, active = True, software = False)
    solutions = Service.objects.filter(service_or_not=False, active = True, software = False)
    setting  = Setting.objects.first()
    

    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_blogs = Blog.objects.all()[0:5]
    
    context = {
        "categories": categories,
        "blogs": blogs,
        "recent_blogs": recent_blogs,
        "tags": tags,
        'setting': setting,
        'services': services,
        'solutions': solutions,

    }    

    
    return render(request, 'blog.html', context)

    
