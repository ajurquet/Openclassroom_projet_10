from rest_framework import serializers
from .models import Issues


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['title',
                  'desc',
                  'tag',
                  'priority',
                  'project_id',
                  'status',
                  'author_user_id',
                  'assignee_user_id',
                  'created_time'
                  ] #TODO trouver pour afficher le nom ou l'email à la place de 'author_user_id'



