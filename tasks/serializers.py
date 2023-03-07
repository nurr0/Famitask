from rest_framework import serializers
from core.serializers import UserSerializer
from .models import *


class ResponsibleSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = ResponsibleOnTask
        fields = ['task', 'responsible_user', 'user_info']
    
    def get_user_info(self, obj):
        user = obj.responsible_user
        serializer = UserSerializer(user)
        return serializer.data

class TaskSerializer(serializers.ModelSerializer):
    user_created = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    responsibles = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_responsibles(self, obj):
        responsibles_query = ResponsibleOnTask.objects.filter(task=obj)
        serialized_data = [ResponsibleSerializer(user).data for user in responsibles_query]
        return serialized_data

class SubTaskSerializer(serializers.ModelSerializer):
    user_created = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = SubTask
        fields = '__all__'
