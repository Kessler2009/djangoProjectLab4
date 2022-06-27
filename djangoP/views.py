from django.http import HttpResponse
from django.shortcuts import render
from .models import Messages
import random

# Create your views here.

users = ["Mikey", "Alex", "Dimas", "Tom", "Daemon"]


def index(request):
    temp = ""
    Messages.objects.create(user=random.choice(users), message=str(random.randint(1, 365345)))
    if not Messages.objects.all():
        return HttpResponse("No Data")
    else:
        for message in Messages:
            temp += str(message)

        return HttpResponse(temp)
