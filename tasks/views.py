from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = [Allo, BasicAuthentication]
    queryset = Task.objects.all()
