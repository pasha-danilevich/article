from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    

    def has_permission(self, request, view, *args):
        read = ['list', 'retrieve']
        write = ['create', 'update', 'partial_update', 'destroy']

        if view.action in read:
            return True
        elif view.action in write:
            return False

                                                                                                
    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if request.user.is_authenticated:
            return True