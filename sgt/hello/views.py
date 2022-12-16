from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, name):
    return render(request, "templates/index.html", {
        "name": name.capitalize()
    })
def greet(request, name):
    return HttpResponse(f'hello, {name}')