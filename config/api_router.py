from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from ethyca_project.games.api.viewsets import GameViewSet, GameMoveViewSet
from ethyca_project.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("games", GameViewSet)
router.register("game-moves", GameMoveViewSet)


app_name = "api"
urlpatterns = router.urls
