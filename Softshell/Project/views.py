from rest_framework.decorators import action, permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        user = request.user

        if project['author_user_id'] == user.user_id:
            project.delete()
            return Response({'message' : 'Projet effacé'})
        else:
            return Response({'message' : "Vous ne pouvez effacer un projet que si vous en êtes l'auteur"}) 





# @action(detail=False, methods=['post', 'put'], permission_classes=[IsAuthenticated])

# if request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# if request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProjectsList(APIView):

#     def get(self, request, format=None):
#         projects = Projects.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HHTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


