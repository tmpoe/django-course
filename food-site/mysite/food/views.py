from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    return HttpResponse(template.render(context={'item_list': item_list}, request=request))

def item(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)