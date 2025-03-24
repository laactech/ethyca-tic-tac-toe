# Ethyca Project

## Set up

1. Ensure you have docker and docker compose installed on your system
2. `Run docker compose build` to build the project
2. `Run docker compose up -d` to run the project
3. `Run docker compose run --rm django python manage.py create_user` and follow the prompts to get your API token

## Playing Tic Tac Toe

1. Make a POST request to the /api/games/ endpoint to create the game
   * ```r = httpx.post("http://localhost:8000/api/games/", json={"game_type": "tic_tac_toe"}, headers={"Authorization": "Token YOUR_API_TOKEN"})```
2. Make a POST request to the /api/game-moves/ endpoint with the ID returned in the /api/games POST request

## Questions

1. Why does this project have celery, redis, rabbitmq, etc?
   * This is a template I use for a lot of projects to get them going fast, and I just decided not to remove them.


