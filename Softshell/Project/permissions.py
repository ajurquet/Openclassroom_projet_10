from rest_framework import permissions
from User.models import Contributor


class IsAuthorOrReadOnly(permissions.BasePermission):
# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.


    def has_permission(self, request):
        message = "Seul un auteur ou contributeur du projet peut effectuer des opérations"

        print(request.user)

        if request.user == request.author:
            return True
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # return request.author == request.user


class IsContributorOrReadOnly(permissions.BasePermission):
# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.
    pass

    # def has_permission(self, request):
    #     message = "Seul un auteur ou contributeur du projet peut effectuer des opérations"


    #     contributors = Contributor.objects.filter(project=request.project)
    #     print(contributors)
        
    #     if request.method in permissions.SAFE_METHODS:
    #         return True

    #     return request.user_contributor == request.user # correspond au related_name de contributor