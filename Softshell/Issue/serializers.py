from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    issue_comment = serializers.StringRelatedField(many=True)

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
        read_only_fields = ['author']

def create(self, validated_data):
        author = self.context.get("request", None).user #récupère le token

        project = Issue.objects.create(
            title = validated_data["title"],
            desc = validated_data["desc"],
            tag = validated_data["tag"],
            priority = validated_data["priority"],
            project = validated_data["project"],
            status = validated_data["status"],
            author = author,
            assignee = validated_data["assignee"],
            created_time = validated_data["created_time"],
            issue_comment = validated_data["issue_comment"],
        )
        project.save()

        return project
