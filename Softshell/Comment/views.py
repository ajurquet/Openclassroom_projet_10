from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsAuthorOrReadOnly


# Les commentaires doivent être visibles par tous les contributeurs au projet
# et par le responsable du projet, mais seul leur auteur
# peut les actualiser ou les supprimer.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() # Faire le filter sur les contributeurs du projet
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])



# class Contributor(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name='user_contributor')
#     project = models.ForeignKey(Project, on_delete=CASCADE, related_name='project_contributor')
