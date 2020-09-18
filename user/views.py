from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from user.serializer import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view



# 允许查看和编辑user 的 API endpoint
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action in ('update',):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]




# 允许查看和编辑group的 API endpoint
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)