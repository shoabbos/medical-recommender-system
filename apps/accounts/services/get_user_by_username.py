from django.contrib.auth.models import User


def get_user_by_username(username):
    return User.objects.get(username=username)
