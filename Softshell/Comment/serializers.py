from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id',
                  'description',
                  'author',
                  'issue',
                  'created_time'
                  ]

