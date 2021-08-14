from Issue.models import Issue
from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import User
from Project.models import Project
from Comment.models import Comment


class UserSerializer(serializers.ModelSerializer):
    # project_created = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    # issue_created = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())
    # issue_assigned = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())
    # comment = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta(object):
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active',
                  'is_admin',
                  'issue_created_by',
                  'issue_assigned_to',
                  'project_created_by',
                  'user_comment',
                  )
        extra_kwargs = {'password': {'write_only': True}}


