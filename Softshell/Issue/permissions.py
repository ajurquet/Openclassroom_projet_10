from rest_framework import permissions

    # Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
    # d'un projet.


class IsContributorOrReadOnly(permissions.BasePermission):
    message = "Seul un auteur ou contributeur du projet peut effectuer des opérations"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
    


