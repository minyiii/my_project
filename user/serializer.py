from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()
# Create your models here.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # password不能省，不然會噴error，就算加了他也不會出現在response中
        fields = ('id', 'url', 'username', 'password', 'email', 'groups')
        # fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    '''def update(self, instance, validated_data):
        username = self.data['user']['username']
        user = User.objects.get(username=username)
        user_data = validated_data.pop('user')
        print(user_data)
        # game_data = validated_data.pop('games')
        print(user)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.update(user, user_data)
        instance.save()
        return instance'''


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
