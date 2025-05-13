from django.http import HttpResponse, JsonResponse


def hello_world(request) -> HttpResponse:
    return JsonResponse({ "message": "Hello, world!" })