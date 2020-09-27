from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from user.serializer import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

# 允许查看和编辑user 的 API endpoint
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        print(self.request.method)
        if self.action in ('create',): # 任何人都可以註冊
            print('creating user!!!!!!!!!')
            self.permission_classes = [AllowAny]
        elif self.action in ('list', 'destroy'):
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    def get_object(self):
        return User.objects.get(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


# 允许查看和编辑group的 API endpoint
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)