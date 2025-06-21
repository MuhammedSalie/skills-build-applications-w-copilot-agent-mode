from django.http import JsonResponse
from django.urls import reverse

def api_root(request):
    # Replace with your Codespace name if needed
    codespace_url = "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "docs": codespace_url + reverse('api-root'),
        "status": "ok"
    })
