from rest_framework import viewsets
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.permissions import IsAuthenticated
from User.models import Contributor

# l'utilisateur ne doit pouvoir appliquer le processus CRUD aux problèmes 
# du projet que si il ou elle figure sur la liste des contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter 
# les problèmes d'un projet.


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all() # Il faut vérifier si l'assigné fait partie des contributeurs
    serializer_class = IssueSerializer
    permission_classes = []

    def get_queryset(self):
        projet_pk = self.kwargs['project_pk']
        contributors = Contributor.objects.filter(project=projet_pk)
        print(contributors)
        
        # Verifie que 
        return Issue.objects.filter(project=self.kwargs['project_pk'])

# & (and), | (or) and ~ (not).

# class Contributor(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name='user_contributor')
#     project = models.ForeignKey(Project, on_delete=CASCADE, related_name='project_contributor')

# class Issue(models.Model):

#     title = models.CharField(max_length=128, blank=False)
#     desc = models.CharField(max_length=128)
#     tag = models.CharField(max_length=12, choices=TAG)
#     priority = models.CharField(max_length=7, choices=PRIORITY)
#     project = models.ForeignKey(Project,
#                                    on_delete=models.CASCADE,
#                                    related_name='issue_related'
#                                    )
#     status = models.CharField(max_length=8, choices=STATUT)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                        on_delete=models.RESTRICT,
#                                        related_name='issue_created_by'
#                                        )
#     assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                          on_delete=models.RESTRICT,
#                                          related_name='issue_assigned_to',
#                                          )
#     created_time = models.DateTimeField(auto_now_add=True)