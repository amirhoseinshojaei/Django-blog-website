from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Blog,Category,Tag,Comment
# Create your views here.

@require_http_methods(["GET"])
def index(request):

    context={}

    return render(request,'blog/home.html',context)


@require_http_methods(['GET'])
def blogs_list(request,category_slug= None):

    category = None
    categories = Category.objects.all()
    blog = Blog.objects.all()

    if category_slug:

        category = get_object_or_404(Category,slug = category_slug)
        blog = Blog.objects.filter(category = category)

    context = {
        'categories':categories,
        'blog':blog,
        'category': category,

    }

    return render (request,'blog/list.html',context)




def blog_detail(request,slug):

    blog = get_object_or_404(Blog,slug=slug)
    category = Category.objects.filter(category=blog)
    tags = Tag.objects.filter(tags=blog)

    context = {
        'blog':blog,
        'category':category,
        'tags':tags
    }

    return render (request,'blog/detail',context)