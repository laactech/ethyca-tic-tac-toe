from rest_framework import viewsets

from ethyca_project.games.api.serializers import GameMoveSerializer, GameSerializer
from ethyca_project.games.models import GameMove, Game


class GameMoveViewSet(viewsets.ModelViewSet):
    queryset = GameMove.objects.all()
    serializer_class = GameMoveSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
