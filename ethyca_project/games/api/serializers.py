from rest_framework import serializers

from ethyca_project.games.models import Game, GameMove


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("game_type", "id")


class GameMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMove
        fields = ("game", "game_state")