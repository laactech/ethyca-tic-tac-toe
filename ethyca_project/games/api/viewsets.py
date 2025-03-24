from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from ethyca_project.games.api.serializers import GameMoveSerializer
from ethyca_project.games.api.serializers import GameSerializer
from ethyca_project.games.models import Game
from ethyca_project.games.models import GameMove


class GameMoveViewSet(viewsets.ModelViewSet):
    queryset = GameMove.objects.all()
    serializer_class = GameMoveSerializer
    ordering_fields = ["created_at"]
    filter_backends = [OrderingFilter]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    ordering_fields = ["created_at"]
    filter_backends = [OrderingFilter]
    ordering = ["-created_at"]

    @action(detail=False, methods=["get"], url_path="my-games")
    def my_games(self, request, pk=None):
        games = Game.objects.filter(game_moves__player=request.user).order_by("-created_at").distinct()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
