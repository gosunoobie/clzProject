from rest_framework import permissions


class UserObjPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")
    SAFE_METHODS =  ('GET', 'HEAD','POST', 'OPTIONS')


    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in self.SAFE_METHODS:
            return True
            
        if user.groups.filter(name='Admin').exists() or obj == request.user:
            return True
        return False

class IsTheUserPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")
    SAFE_METHODS =  ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name='Admin').exists() or obj == request.user:
            return True
        return False
