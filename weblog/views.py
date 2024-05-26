from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Blog,Category,Tag,Comment
from django.http import JsonResponse
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


@require_http_methods(['GET', 'POST'])
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all()
    category = blog.category
    tags = blog.tag.all()

    if request.method == "POST":
        json_response = {
            'blog': {
                'title': blog.title,
                'description': blog.description,
                'image': blog.image.url if blog.image else None,
                'published_at': blog.published_at.isoformat(),
                'updated_at': blog.updated_at.isoformat(),
                'user': blog.user.username,
                'slug': blog.slug,
                'category': category.name,
                'tags': [tag.name for tag in tags]
            },
            'comments': [
                {
                    'body': comment.body,
                    'user': comment.user.username,
                    'date': comment.date.isoformat()
                } for comment in comments
            ]
        }
        return JsonResponse(json_response)

    context = {
        'blog': blog,
        'comments': comments,
        'category': category,
        'tags': tags
    }
    return render(request, 'blog/detail.html', context)