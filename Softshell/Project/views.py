from rest_framework import request, viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor, IsContributor
from .models import Project
from .serializers import ProjectSerializer
from User.models import Contributor


# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.



class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all() # seul l'auteur ou les contributeur peuvent voir 
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated&IsAuthor&IsContributor]
   
    def get_queryset(self):
        contributors = Contributor.objects.filter(user=self.request.user)

        # "project_contribor" correspond au related_name de "projet" dans le modèle "Contributor"
        return Project.objects.filter(project_contributor__in=contributors)|Project.objects.filter(author=self.request.user)


# & (and), | (or) and ~ (not).

# class Contributor(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name='user_contributor')
#     project = models.ForeignKey(Project, on_delete=CASCADE, related_name='project_contributor')