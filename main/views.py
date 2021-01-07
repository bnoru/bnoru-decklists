from django.shortcuts import render
from django.http import HttpResponse
from .models import Decklist

def homepage(request):
    return render (request=request,
                   template_name="main/home.html",
                   context={"decklists": Decklist.objects.all})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})