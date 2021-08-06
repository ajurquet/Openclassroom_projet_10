from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Users
        fields = ('user_id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active',
                  'is_admin',
                  )
        extra_kwargs = {'password': {'write_only': True}}