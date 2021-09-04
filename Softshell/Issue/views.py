from rest_framework import viewsets
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.permissions import IsAuthenticated

# l'utilisateur ne doit pouvoir appliquer le processus CRUD aux problèmes 
# du projet que si il ou elle figure sur la liste des contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter 
# les problèmes d'un projet.


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all() # Il faut vérifier si l'assigné fait partie des contributeurs
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

# & (and), | (or) and ~ (not).