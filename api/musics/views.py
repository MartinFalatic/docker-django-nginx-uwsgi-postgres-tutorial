# Create your views here.
from musics.models import Music
from musics.serializers import MusicSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    # An action target function CANNOT be named `detail`
    # See also https://github.com/encode/django-rest-framework/issues/6083

    # /api/music/{pk}/detail/
    @action(detail=True, methods=['get'], url_path='detail', url_name='detail')
    def one_singer(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song,
        }
        return Response(result, status=status.HTTP_200_OK)

    # /api/music/all_singer/
    @action(detail=False, methods=['get'])
    def all_singer(self, request):
        music = Music.objects.values_list('singer', flat=True).distinct()
        return Response(music, status=status.HTTP_200_OK)
