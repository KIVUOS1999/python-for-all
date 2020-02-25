from django.shortcuts import render
from .models import Tutorial
from django.http import HttpResponse

def homepage(request):
        return render(request, "home.html", {"tutorials":Tutorial.objects.all()})

def item(request, item_id):
    
    itm = Tutorial.objects.get(id = item_id)
    return render(request, 'home.html', {'item':itm, "tutorials":Tutorial.objects.all()})