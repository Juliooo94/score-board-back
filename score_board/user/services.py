from django.contrib.auth import authenticate, login
from rest_framework.request import Request
from score_board.user.models import User


def log_user_in(request: Request, username:str, password: str) -> User:
    user = authenticate(request, username=username, password=password)
    if not user:
        if User.objects.filter(username=username).exists():
            raise ValueError('Password issue')
        else:
            user = User.objects.create_user(username=username, password=password)
    login(request, user)
    return user
