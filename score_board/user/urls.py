from django.urls import path

from score_board.user.views.authentification import LoginOrSignupView, MeView

urlpatterns = [
    path("login", LoginOrSignupView.as_view(), name="auth"),
    path("me", MeView.as_view(), name="me"),
]
