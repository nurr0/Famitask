from rest_framework import serializers

from .models import *


class TaskSerializer(serializers.ModelSerializer):
    user_created = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # responsible = 
    class Meta:
        model = Task
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    user_created = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = SubTask
        fields = '__all__'

class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibleOnTask
        fields = '__all__'