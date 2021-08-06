from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id',
                  'description',
                  'author_user_id',
                  'issue_id',
                  'created_time'
                  ] #TODO trouver pour afficher le nom ou l'email à la place de 'author_user_id'

