#  permission if user is the owner of the data

from rest_framework import permissions

class UserIsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
    