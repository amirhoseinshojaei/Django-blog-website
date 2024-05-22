from django.urls import path
from . import views


app_name = 'blog'

urlpatterns=[
    path('',views.index,name='home'),
    path('blogs/',views.blogs_list,name='blogs'),
    path('<slug:category_slug>/',views.blogs_list,name='blog_list_by_category'),
    path('blog/<slug:slug>',views.blog_detail,name='blog_detail'),
]