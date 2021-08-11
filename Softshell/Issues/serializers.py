from Comments.models import Comments
from rest_framework import serializers
from .models import Issues


class IssuesSerializer(serializers.ModelSerializer):
    Comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comments.objects.all())
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
                  'created_time',
                  'Comments'
                  ] #TODO trouver pour afficher le nom ou l'email à la place de 'author_user_id'


# class Comments(models.Model):
 
#     issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='Comments')
