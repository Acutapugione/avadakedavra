from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from . models import Author, News


def index(request):
    items = News.objects.order_by("-pub_date")[:5]

    context = {
        "base_url": "news",
        "items": items,
    }
    return render(request, "crud/read.html", context)


def details(request, id):
    item = get_object_or_404(News, pk=id)

    context = {
        "base_url": "news",
        "item": item,
    }
    return render(request, "crud/details.html", context)