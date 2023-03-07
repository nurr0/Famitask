from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')
        queryset = Task.objects.filter(group_id=group_id)
        return queryset

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] 


class SubtaskList(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        parent_task_id = self.kwargs.get('parent_task_id')
        queryset = SubTask.objects.filter(parent_task_id=parent_task_id)
        return queryset


class SubtaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]


class ResponsibleOnTaskList(generics.ListAPIView):
    serializer_class = ResponsibleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        queryset = ResponsibleOnTask.objects.select_related('responsible_user').filter(task_id=task_id)
        return queryset


class ResponsibleOnTaskCreate(generics.CreateAPIView):
    serializer_class = ResponsibleSerializer
    permission_classes = [IsAuthenticated]


class ResponsibleOnTaskDelete(generics.DestroyAPIView):
    queryset = ResponsibleOnTask.objects.all()
    serializer_class = ResponsibleSerializer
    permission_classes = [IsAuthenticated]

