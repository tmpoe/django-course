from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Item
from .forms import ItemForm


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request,'food/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request, item_id: int):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'food/item.html', {'item': item})


class AddItemView(CreateView):
    model = Item
    template_name = 'food/item_form.html'
    fields = ['name', 'description', 'price', 'image']

    def form_valid(self, form):
        item_form_instance: Item = form.instance
        item_form_instance.user_name = self.request.user
        return super().form_valid(form)


def edit_item(request, item_id: int):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item_form.html', {'form': form})


def delete_item(request, item_id: int):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item_delete.html', {'item': item})
