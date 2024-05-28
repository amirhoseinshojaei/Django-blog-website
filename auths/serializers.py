from rest_framework import serializers
from . models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_lenght = 255 , read_only = True)
    last_name = serializers.CharField(max_length = 255 , read_only = True)
    username = serializers.CharField(max_length=255, read_only=True)
    email = serializers.EmailField(max_length = 255, read_only = True)

    class Meta:

        model = CustomUser
        fields = [

            'first_name','last_name',
            'username','password','email'
        ]