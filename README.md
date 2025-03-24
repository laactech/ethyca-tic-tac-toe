# Ethyca Project

## Set up

1. Ensure you have docker and docker compose installed on your system
2. `Run docker compose build` to build the project
2. `Run docker compose up -d` to run the project
3. `Run docker compose run --rm django python manage.py create_user` and follow the prompts to get your API token

## Playing Tic Tac Toe

API Documentation located at http://localhost:8000/api/docs/

1. Make a POST request to the /api/games/ endpoint to create the game
   * ```r = httpx.post("http://localhost:8000/api/games/", json={"game_type": "tic_tac_toe"}, headers={"Authorization": "Token YOUR_API_TOKEN"})```
2. Make a POST request to the /api/game-moves/ endpoint with the ID returned in the /api/games POST request
   * ```r = httpx.post("http://localhost:8000/api/game-moves/", json={"next_move": {"x": 1, "y": 1}, "game": "YOUR_GAME_ID"}, headers={"Authorization": "Token YOUR_API_TOKEN"})```
3. Make a few more game-move POST requests
4. Make a GET request to the /api/game-moves/ endpoint to see the moves in chronological order
   * ```r = httpx.get("http://localhost:8000/api/game-moves/", headers={"Authorization": "Token YOUR_API_TOKEN"})```
5. Make a GET request to the /api/games/my-games/ endpoint to see your games
   * ```r = httpx.get("http://localhost:8000/api/games/my-games/", headers={"Authorization": "Token YOUR_API_TOKEN"})```

## Question and Answer

1. How much time you spent building the project
   * About 2 and a half hours
1. Any assumptions you made
   * I assumed that the human player is always X's
   * I assumed I didn't need to account for two human players
1. Any trade-offs you made
   * I didn't really implement "winning"
   * I didn't write tests (tests are great though)
   * I didn't add a player ForeignKey to the "Game" model, but I probably should have
1. Any special/unique features you added
   * The computer will randomly play a move against you and won't overwrite any existing move
   * I added a lot of validation and returned some nice error messages when you get a POST body wrong
   * The API endpoints are behind actual authentication
   * There is API documentation (although not the best)
   * You should be able to change the ordering with the "ordering" query parameter
1. Anything else you want us to know about
   * The next step in this project would be writing tests, but I opted to just document it instead of doing it.
   * If this were going to production, I'd add a bunch of logging for easier debugging.
   * This project has stuff like redis, celery, rabbitmq, and a bunch of unused packages because this is just the Django starter template I use for a lot of stuff
1. Any feedback you have on this technical challenge
   * I enjoyed this coding test. It's way better than the leetcode stuff
