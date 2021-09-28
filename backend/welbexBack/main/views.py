from django.http import HttpResponse, JsonResponse
from .models import Main

def index(request):
    res = []
    for data in list(Main.objects.all()):
        res.append({'date': data.date, 'title': data.title, 'quantity': data.quantity, 'distance': data.distance})
    return JsonResponse(res, safe=False)
