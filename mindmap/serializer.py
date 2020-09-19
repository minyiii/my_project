from rest_framework import serializers
from .models import Mindmap
from django.contrib.auth.models import User, Group

class MindmapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Mindmap
        # fields = '__all__'
        # fields = ['id','author','describe','md_file' ,'json_file']
        fields = ['id','author','describe', 'json_file'] # respnse給前端的東西(id是auto field，預設read only)
