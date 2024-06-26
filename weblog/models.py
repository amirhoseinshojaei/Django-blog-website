from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField()
    published_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta:

        verbose_name_plural = 'Categories'
        ordering = ('published_at',)


    def get_absolute_url(self):

        return reverse('blog:blog_list_by_category',args=[self.slug])


    def __str__(self):

        return self.name



class Tag(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    published_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

    def get_absolute_url(self):

        return reverse('blog:blog_by_tags',args=[self.slug])

    class Meta:

        verbose_name_plural = 'Tags'
        ordering = ('published_at',)

    def __str__(self):

        return self.name




class Blog(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='blogs/%Y%m%d',null=True)
    published_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    category = models.ForeignKey(Category,related_name='blog',on_delete= models.CASCADE)
    tag = models.ManyToManyField(Tag,related_name='blogs')


    def get_absolute_url(self):

        return reverse('blog:blog_detail',args=[self.slug])


    class Meta:

        verbose_name_plural = 'Blogs'
        ordering = ('published_at',)

    def __str__(self):

        return self.title




class Comment(models.Model):

    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):

        return self.user.email        