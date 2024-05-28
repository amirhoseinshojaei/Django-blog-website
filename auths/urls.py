from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter
app_name = 'auth'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.login,name='signin'),
    path('logout/',views.logout,name='logout'),
]

router = SimpleRouter()
router.register('users/',views.UserViewSet,basename='users')
urlpatterns+=router.urls