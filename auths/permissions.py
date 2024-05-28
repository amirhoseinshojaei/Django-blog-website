from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
    

        if request.user.is_superuser:

            return request.method in ['GET','PUT','POST','DELETE']
    
        if request.user.is_staff:

            return request.method in ['GET']
    
        return False