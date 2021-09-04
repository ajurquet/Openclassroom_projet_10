from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # Les commentaires doivent être visibles par tous les contributeurs au projet
    # et par le responsable du projet, mais seul leur auteur
    # peut les actualiser ou les supprimer.


    def has_object_permission(self, request, view, obj):
        message = "Seul l'auteur du commentaire peut actualiser ou supprimer"
        
        if request.method in permissions.SAFE_METHODS: # "method" correspond ici à GET, PUT etc.....
            return True # True correspond ici à "read only"

        return obj.author == request.user