from rest_framework import viewsets

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])