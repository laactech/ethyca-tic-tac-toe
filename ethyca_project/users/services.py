from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction

User = get_user_model()


def create_new_user(
    email: str,
    password: str | None = None,
    user_full_name: str | None = None,
    *,
    is_superuser: bool = False,
    save: bool = True,
) -> tuple[User, EmailAddress]:
    with transaction.atomic():
        if password is None:
            password = "password"  # noqa: S105
        kwargs = {
            "password": make_password(password),
            "email": email,
            "is_superuser": is_superuser,
            "is_staff": is_superuser,
        }
        if user_full_name is not None:
            kwargs["name"] = user_full_name
        user = User(**kwargs)
        email_obj = EmailAddress(user=user, email=email, primary=True, verified=True)
        if save is True:
            user.save()
            email_obj.save()
        return user, email_obj
