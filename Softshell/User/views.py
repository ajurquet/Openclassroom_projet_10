from rest_framework import viewsets
from .models import User, Contributor
from .serializers import UserSerializer, ContributorSerializer
from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.all()
        # return Contributor.objects.filter(project=self.kwargs['project_pk'])|Contributor.objects.filter(user=self.kwarg['user_pk]'])





    # Faire ca pour le signup :
 
    # @action(methods=['post'], detail=True, permission_classes=[IsAdminOrIsSelf])
    # def set_password(self, request, pk=None):

    # The following route would be generated:
    # URL pattern: ^users/{pk}/set_password/$
    # URL name: 'user-set-password'

    # By default, the URL pattern is based on the method name, and the URL name is the combination of the ViewSet.basename
    # and the hyphenated method name. If you don't want to use the defaults for either of these values, you can instead 
    # provide the url_path and url_name arguments to the @action decorator.

    # For example, if you want to change the URL for our custom action to ^users/{pk}/change-password/$, you could write:

    # @action(methods=['post'], detail=True, permission_classes=[IsAdminOrIsSelf],
    #         url_path='change-password', url_name='change_password')
    # def set_password(self, request, pk=None):