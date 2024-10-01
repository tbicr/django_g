import time

from django.http import HttpResponse


time.sleep(10)

def index(request):
    return HttpResponse("Ok")
