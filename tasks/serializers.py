from rest_framework import serializers

from .models import *


class TaskSerializer(serializers.ModelSerializer):
    user_created = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'

