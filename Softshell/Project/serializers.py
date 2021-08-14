from Issue.models import Issue
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    Issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())
    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author_user_id', 'issue_related']


