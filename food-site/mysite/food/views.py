from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request,'food/index.html', context)

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'food/item.html', {'item': item})
