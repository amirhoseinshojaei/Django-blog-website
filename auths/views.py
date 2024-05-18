from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
# Create your views here.

@csrf_exempt
def signup(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')

        if not all([first_name,last_name,phone,email,age,password]):

            return JsonResponse({'error':'All fields are required'},
                                status = 400)
        # Checking that there is no user with the same email or username
        if CustomUser.objects.filter(email=email).exists():

            return JsonResponse({
                'error':'User with this email is Already exist'
            },status = 400)
        
        # Create new user
        try:
            new_user = CustomUser.objects.create(

                first_name = first_name,
                last_name = last_name,
                phone = phone,
                email = email,
                age = age,
                password = make_password(password)
            )
            # Config username
            new_user.username = f'{first_name} {last_name}'
            #Save new user
            new_user.save()

            #New user authentication
            new_user = authenticate(request,username = new_user.username,email=email,password = password)

            # Login new_user
            if new_user is not None:

                login(request,new_user)
                return JsonResponse({
                    'success': 'Success Login'
                },status = 200)
            
            return JsonResponse({
                'error':'Authentication failed'
            },status = 400)
        
        except Exception as e:

            return JsonResponse({
                'error':str(e)
            },status = 400)
    
    else:

        return render(request,'auths/signup.html')
