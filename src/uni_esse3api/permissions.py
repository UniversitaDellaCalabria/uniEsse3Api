from rest_framework import permissions

from . settings import ESSE3_PREFIX


def checkUniEsse3ApiGroupPermission(group_name):
    """
    Factory che restituisce una classe di permesso configurata 
    per un gruppo specifico.
    """
    class uniEsse3ApiPermission(permissions.IsAuthenticated):
        def has_permission(self, request, view):
            user = request.user
            if user.is_superuser: return True
            return user.groups.filter(name=f'{ESSE3_PREFIX}-{group_name}').exists()

    # Restituiamo la classe (NON un'istanza della classe)
    return uniEsse3ApiPermission
