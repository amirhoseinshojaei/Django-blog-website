from . import views
from django.urls import path

app_name = 'auth'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
]