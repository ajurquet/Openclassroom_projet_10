from Issues.models import Issues
from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import Users
from Projects.models import Projects
from Comments.models import Comments


class UserSerializer(serializers.ModelSerializer):
    Projects_created = serializers.PrimaryKeyRelatedField(many=True, queryset=Projects.objects.all())
    Issues_created = serializers.PrimaryKeyRelatedField(many=True, queryset=Issues.objects.all())
    Issues_assigned = serializers.PrimaryKeyRelatedField(many=True, queryset=Issues.objects.all())
    Comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comments.objects.all())

    class Meta(object):
        model = Users
        fields = ('user_id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active',
                  'is_admin',
                  'Projects_created',
                  'Issues_created',
                  'Issues_assigned',
                  'Comments',
                  )
        extra_kwargs = {'password': {'write_only': True}}
