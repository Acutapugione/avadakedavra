from django.shortcuts import render
from django.http import HttpResponse
from . models import Question

# Create your views here.
def index(request):
    context = {"questions": Question.objects.all()}
    return render(request, 'index.html', context=context)

# Create your views here.
def edit(request):
    return HttpResponse("How dare you! Wanna me to edit!")