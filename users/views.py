import json
from django.http import HttpResponse
from django.shortcuts import render

from users.models import UsersModel

# Create your views here.
def LoginView(request):
    print(request)
    email = json.loads(request.body)
    user = UsersModel.objects.filter(email= email["email"])
    print(user)
    return HttpResponse(
        {
            "message": "Logged in"
        }
    )

def SignupView(request):
    print(request.body)
    email = json.loads(request.body)
    
    UsersModel.objects.create(
        _id=email["id"],
        email=email["email"],
        name="some name"
    )
    print(UsersModel.objects.all())
    return HttpResponse({
        "message": "Logged out"
    })
