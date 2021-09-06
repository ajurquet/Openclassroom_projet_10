from rest_framework import serializers
from .models import Project
from User.models import Contributor


class ProjectSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        project = Project.objects.create(
            title = validated_data["title"],
            description = validated_data["description"],
            type = validated_data["type"],
            author = validated_data["author"],
            # issue_related = validated_data["issue_related"],
        )
        project.save()

        contributor = Contributor.project.create(
            user = validated_data["project_created_by"],
            project = validated_data["project_contributor"],

        )

        contributor.save()

        

        return project



# class Contributor(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name='user_contributor')
#     project = models.ForeignKey(Project, on_delete=CASCADE, related_name='project_contributor')


