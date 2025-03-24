import getpass
import sys

from django.core.management.base import BaseCommand
from django.db import transaction
from rest_framework.authtoken.models import Token

from ethyca_project.users.services import create_new_user


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = input("Enter the email to use for your user: ")  # nosec
        name = input("Enter your name: ")  # nosec
        password = getpass.getpass("Enter your desired password: ")  # nosec
        with transaction.atomic():
            user, _ = create_new_user(
                email,
                password=password,
                is_superuser=True,
                user_full_name=name,
            )
            token = Token.objects.create(user=user)
            print(f"Your API token: {token.key}")
