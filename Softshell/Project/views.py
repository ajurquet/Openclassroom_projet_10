from rest_framework import request, viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly, IsContributorOrReadOnly
from .models import Project
from .serializers import ProjectSerializer
from User.models import Contributor


# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.



class ProjectViewSet(viewsets.ModelViewSet, IsAuthorOrReadOnly, IsContributorOrReadOnly):

    queryset = Project.objects.all() # seul l'auteur ou les contributeur peuvent voir 
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated&IsAuthorOrReadOnly|IsContributorOrReadOnly]
    # permission_classes = [IsAuthenticated&IsAuthor]
   
    # def get_queryset(self):
    #     contributors = Contributor.objects.filter()
    #     print(contributors)
    #     return Project.objects.filter()



# & (and), | (or) and ~ (not).

# class Contributor(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name='user_contributor')
#     project = models.ForeignKey(Project, on_delete=CASCADE, related_name='project_contributor')