from rest_framework import serializers

from .models import *


class GroupSerializer(serializers.ModelSerializer):
    user_created = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Group
        fields = '__all__'


class UserGroupRelationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserGroupRelation
        fields = '__all__'
