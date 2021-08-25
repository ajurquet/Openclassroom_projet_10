from Comment.models import Comment
from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    # Comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    class Meta:
        model = Issue
        fields = ['id', 
                  'title',
                  'desc',
                  'tag',
                  'priority',
                  'project',
                  'status',
                  'author',
                  'assignee',
                  'created_time',
                  'issue_comment'
                  ]


