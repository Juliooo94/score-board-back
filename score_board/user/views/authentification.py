from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.middleware.csrf import get_token
from rest_framework.request import Request

from score_board.user.serializers.user import UserSerializer
from score_board.user.services import log_user_in


class LoginOrSignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> JsonResponse:
        username: str | None = request.data.get('username')
        password: str | None = request.data.get('password')
        if not username or not password:
            return JsonResponse({'error': 'Username and password required'}, status=400)
        try:
            user = log_user_in(request, username, password)
        except ValueError:
            return JsonResponse({'error': 'Wrong password | Username already taken'}, status=403)
        return JsonResponse({'success': True, 'username': user.username, 'csrfToken': get_token(request)})


class MeView(APIView):
    def get(self, request: Request) -> JsonResponse:
        if request.user.is_authenticated:
            serialized_user = UserSerializer(request.user)
            return JsonResponse({
                "data": serialized_user.data,
            }, status=200)
        else:
            return JsonResponse({"error": "Not authenticad"}, status=401)
