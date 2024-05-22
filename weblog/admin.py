from django.contrib import admin
from .models import Blog,Comment,Category,Tag
# Register your models here.

class CommentTabularInline(admin.TabularInline):

    model = Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    inlines = [CommentTabularInline,]

    list_display = [
        'title',
        'slug',
        'user',
        'published_at',
        'updated_at',
        'category'
    ]

    list_display_links = ['title']

    list_editable = ['slug']

    list_filter = ['published_at','updated_at']

    list_per_page = 150

    list_max_show_all = 150

    date_hierarchy = "published_at"

    prepopulated_fields ={'slug':('title',)}

    list_select_related = ['category','user']

    def category_name(self,obj):

        return obj.category.name
    
    def user_email(self,obj):

        return obj.user.email


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug','published_at','updated_at']

    list_display_links = ['name']

    list_editable = ['slug']

    list_filter = ['published_at','updated_at']

    list_max_show_all = 150

    list_per_page = 150

    prepopulated_fields = {'slug':('name',)}
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = [
        'name','slug',
        'published_at','updated_at'
    ]

    list_display_links = ['name']

    list_editable = ['slug']

    list_filter = ['published_at','updated_at']

    list_max_show_all = 150

    list_per_page = 150

    prepopulated_fields = {'slug':('name',)}



admin.site.register(Comment)