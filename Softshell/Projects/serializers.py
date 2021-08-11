from Issues.models import Issues
from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    Issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issues.objects.all())
    class Meta:
        model = Projects
        fields = ['title', 'description', 'type', 'author_user_id', 'Issues']


