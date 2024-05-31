from rest_framework import serializers
from .models import Blog,Comment,Category,Tag
from auths.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tag
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ['username','email']



class BlogSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many = False)
    tag = TagSerializer(many = True)
    user = UserSerializer(many = False)

    class Meta:

        model = Blog
        fields = [

            'title','slug',
            'image','user',
            'category','tag',
            'published_at','updated_at'
        ]