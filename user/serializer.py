from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()
# Create your models here.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')
        # fields = '__all__'



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')