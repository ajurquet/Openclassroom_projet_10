from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'type', 'author_user_id'] #TODO trouver pour afficher le nom ou l'email à la place de 'author_user_id'

