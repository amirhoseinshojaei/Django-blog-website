from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Blog,Category,Tag,Comment
from django.http import JsonResponse,HttpResponseForbidden,HttpResponseNotAllowed
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
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



@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            blog = Blog.objects.create(
                
                title=data['title'],
                slug=data['slug'],
                description=data['description'],
                image=data.get('image'),
                user=request.user,
                category=Category.objects.get(id=data['category']),
            )
            blog.tag.set(Tag.objects.filter(id__in=data['tags']))
            blog.save()
            return JsonResponse({'message': 'Blog created successfully!', 'blog': {
                'id': blog.id,
                'title': blog.title,
                'slug': blog.slug,
                'description': blog.description,
                'image': blog.image.url if blog.image else None,
                'published_at': blog.published_at.isoformat(),
                'updated_at': blog.updated_at.isoformat(),
                'user': blog.user.username,
                'category': blog.category.name,
                'tags': [tag.name for tag in blog.tag.all()]
            }})
        except Exception as e:

            return JsonResponse({'error': str(e)}, status=400)
        
    return HttpResponseNotAllowed(['POST'])

        

@login_required
@require_http_methods(['PUT'])
@csrf_exempt
def blog_update(request,slug):

    blog = get_object_or_404(Blog,slug=slug)
    if request.user != blog.user:

        return HttpResponseForbidden("You are not allowed to edit this blog")
    
    if request.method == "PUT":

        try:
            data = json.loads(request.body)
            blog.title = data['title']
            blog.description = data['description']
            if data.get('image'):

                blog.image = data['image']
            
            blog.category = data['category']
            blog.tag.set(Tag.objects.filter(id__in=data['tags']))

            blog.save()
            return JsonResponse({'message':'Blog updated succesfully','blog':{

                'id' : blog.id,
                'title': blog.title,
                'slug':blog.slug,
                'description': blog.description,
                'image': blog.image.url if blog.image else None,
                'published_at': blog.published_at.isoformat(),
                'updated_at': blog.updated_at.isoformat(),
                'user': blog.user.username,
                'category': blog.category,
                'tags':[ tag.name for tag in blog.tag.all()]
            }})
        except Exception as e:

            return JsonResponse({'error':str(e)},status = 400)
    
    return HttpResponseNotAllowed(['PUT'])


@login_required
@require_http_methods(['DELETE'])
@csrf_exempt
def blog_delete(request,slug):

    blog = get_object_or_404(Blog,slug=slug)

    if request.user != blog.user:

        return HttpResponseForbidden("You are not allowed to delete this blog")
    
    if request.method == 'DELETE':

        blog.delete()
        return JsonResponse({'message':'Blog deleted succesfully'},status = 200)
    
    return HttpResponseForbidden(['DELETE'])