from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class GroupCreateAPIView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class GroupAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        user_group = UserGroupRelation.objects.filter(user=self.request.user)
        return Group.objects.filter(pk__in=user_group)


class UserGroupRelationCreateAPIView(generics.CreateAPIView):
    serializer_class = UserGroupRelationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]



