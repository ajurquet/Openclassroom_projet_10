from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active',
                  'is_admin',
                  'issue_created_by',
                  'issue_assigned_to',
                  'project_created_by',
                  'user_comment',
                  'user_contributor',
                  )
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()
        return user


