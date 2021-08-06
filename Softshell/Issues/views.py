from rest_framework import viewsets

from .models import Issues
from .serializers import IssuesSerializer


class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    permission_classes = []