from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *

class GroupListCreateView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получить текущего пользователя
        user = self.request.user

        # Получить связанные с пользователем группы
        user_groups = UserGroupRelation.objects.filter(user=user).select_related('group').values_list('group', flat=True)

        # Получить объекты Group связанные с текущим пользователем
        queryset = Group.objects.filter(pk__in=user_groups, is_active=True)

        return queryset

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        # Получить текущего пользователя
        user = self.request.user

        # Получить связанные с пользователем группы
        user_groups = UserGroupRelation.objects.filter(user=user).select_related('group').values_list('group', flat=True)

        # Получить объекты Group связанные с текущим пользователем
        queryset = Group.objects.filter(pk__in=user_groups, is_active=True)

        return queryset


class UserGroupRelationList(generics.ListAPIView):
    serializer_class = UserGroupRelationSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return UserGroupRelation.objects.filter(group_id=group_id).select_related('user')


class UserGroupRelationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserGroupRelationSerializer

    def get_queryset(self):
        relation_pk = self.kwargs['pk']
        return UserGroupRelation.objects.filter(pk=relation_pk)


class UserGroupRelationCreate(generics.CreateAPIView):
    serializer_class = UserGroupRelationCreateSerializer
