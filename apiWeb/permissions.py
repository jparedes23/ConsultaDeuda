from rest_framework.permissions import BasePermission
from .models import UsuarioModel

class SoloAdministradores(BasePermission):
    message ='solamente los Administradores pueden realizar esta accion'

    def has_permission(self, request, view):
        print(request.user)
        usuario:UsuarioModel = request.user

        print(request.auth)
        print(usuario.tipoUsuario)
        if usuario.tipoUsuario == 'ADMINISTRADOR':
            return True
        else:
            return False
        
class SoloClientes(BasePermission):
    message = 'Puede ver su deuda'

    def has_permission(self, request, view):
        usuario:UsuarioModel = request.user
        if usuario.tipoUsuario == 'CLIENTE':
            return True
        else:
            return False