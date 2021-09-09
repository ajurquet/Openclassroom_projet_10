from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from .models import Project
from .serializers import ProjectSerializer
from User.models import Contributor

# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthorOrReadOnly]
   
    def get_queryset(self): 
        contributors = Contributor.objects.filter(user=self.request.user)
        for contributor in contributors:
            print(contributor.user)

        Project.objects.filter(project_contributor__in=contributors)
        print(f"user in contributors : {contributors}")
        
        user = self.request.user

        # project_contributor correspond au related_name de "projet" dans le modèle Contributor
        return (Project.objects.filter(author=self.request.user)|Project.objects.filter(project_contributor__in=contributors)).distinct()


# & (and), | (or) and ~ (not).
