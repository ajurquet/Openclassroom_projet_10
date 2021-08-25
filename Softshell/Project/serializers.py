from Issue.models import Issue
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # Issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author',
                  'issue_related',
                  'project_contributor',
                  ]


