from rest_framework import serializers

from ethyca_project.games.models import Game
from ethyca_project.games.models import GameMove
from ethyca_project.games.services import get_default_tic_tac_toe_state
from ethyca_project.games.services import place_random_o


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("game_type", "id")


class GameMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMove
        fields = ("game", "game_state", "next_move")
        read_only_fields = ("game_state",)

    next_move = serializers.DictField(write_only=True)

    def create(self, validated_data):
        game = validated_data["game"]
        next_move = validated_data["next_move"]
        next_move_x = next_move["x"]
        next_move_y = next_move["y"]
        player = validated_data["player"]

        try:
            latest_game_move = GameMove.objects.filter(game=game).latest("created_at")
            latest_game_state = latest_game_move.game_state
        except GameMove.DoesNotExist:
            latest_game_state = get_default_tic_tac_toe_state()

        latest_game_state[next_move_x][next_move_y] = "x"
        latest_game_state = place_random_o(latest_game_state)

        return GameMove.objects.create(game=game, game_state=latest_game_state, player=player)

    def validate(self, data):
        next_move = data["next_move"]
        game = data["game"]
        try:
            latest_game_move = GameMove.objects.filter(game=game).latest("created_at")
            latest_game_state = latest_game_move.game_state
        except GameMove.DoesNotExist:
            latest_game_state = get_default_tic_tac_toe_state()

        if "x" not in next_move or "y" not in next_move:
            raise serializers.ValidationError("next_move must contain both 'x' and 'y'")

        next_move_x = next_move["x"]
        next_move_y = next_move["y"]

        if not (0 <= next_move_x < 3 and 0 <= next_move_y < 3):
            raise serializers.ValidationError("next_move 'x' and 'y' must be either 0, 1, or 2")

        if latest_game_state[next_move_x][next_move_y] != ".":
            raise serializers.ValidationError("next_move invalid because coordinates already occupied")

        return data
