from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from .models import Mindmap
from .serializer import MindmapSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class MindmapsViewSet(viewsets.ModelViewSet):
    queryset = Mindmap.objects.all()
    serializer_class = MindmapSerializer
    permission_classes = (IsAuthenticated,)

    # POST，回傳JSON


    # 取得單一個json檔(編輯頁面)
    # http://127.0.0.1:8000/api/mindmaps/{id}/edit
    @action(detail=True, methods=['get'])
    def edit(self, request, pk=None):
        mm = get_object_or_404(Mindmap, pk=pk)
        result = { # ''內是response中的欄位名、mm.?要看model中設定的欄位名
            'id': mm.id,
            'json': mm.json_file
        }
        return Response(result, status=status.HTTP_200_OK)

    # 還沒好
    @action(detail=False, methods=['get'])
    def all(self, request):
        # mm = queryset.filter(author = request.author)
        mm = Mindmap.objects.get(author = request.author)
        serializer = MindmapSerializer(mm, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(result, status=status.HTTP_200_OK)