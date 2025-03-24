import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GamesConfig(AppConfig):
    name = "ethyca_project.games"
    verbose_name = _("Games")
