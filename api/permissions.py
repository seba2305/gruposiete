from rest_framework.permissions import BasePermission

class IsOrganizacionSectorial(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='organizacion_sectorial').exists()
    
 
class IsOrganizacionSectorialOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name='organizacion_sectorial').exists())