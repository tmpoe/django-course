from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the food index.")

def item(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)