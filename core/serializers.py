from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class UserGroupRelationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserGroupRelation
        fields = ['id', 'user', 'group']


class UserGroupRelationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroupRelation
        fields = ['id', 'user', 'group']


class GroupSerializer(serializers.ModelSerializer):
    user_group_relation = UserGroupRelationSerializer(
        many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'is_active',
                  'user_created', 'date_created', 'user_group_relation']
        read_only_fields = ['user_created']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['is_active'] = True

        group = Group.objects.create(user_created=user, **validated_data)
        UserGroupRelation.objects.create(user=user, group=group)

        return group
