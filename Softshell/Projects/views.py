
from rest_framework import viewsets

from .models import Projects
from .serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []
   



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


