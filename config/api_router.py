from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from ethyca_project.applications.api.viewsets import SchoolApplicationViewSet
from ethyca_project.documents.api.viewsets import DocumentViewSet
from ethyca_project.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("school-applications", SchoolApplicationViewSet)
router.register("documents", DocumentViewSet)


app_name = "api"
urlpatterns = router.urls
