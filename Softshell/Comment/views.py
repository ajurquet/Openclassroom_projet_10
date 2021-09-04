from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Les commentaires doivent être visibles par tous les contributeurs au projet
# et par le responsable du projet, mais seul leur auteur
# peut les actualiser ou les supprimer.

# Seuls les contributeurs peuvent créer (Create) et lire (Read)
# les commentaires relatifs à un problème. En outre, ils ne peuvent les
# actualiser (Update) et les supprimer (Delete) que s'ils en sont les auteurs.


class CommentViewSet(viewsets.ModelViewSet, IsAuthorOrReadOnly):
    queryset = Comment.objects.all() # Faire le filter sur les contributeurs du projet
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly&IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])

# & (and), | (or) and ~ (not).
