from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy

from items.models import Item


def item_create(request):
    data = {}
    if request.method == 'POST':
        data['name'] = request.POST.get('name')
        data['description'] = request.POST.get('description')
        data['price'] = request.POST.get('price', '')
        data['code'] = request.POST.get('code', '')
        data['is_available'] = bool(request.POST.get('is_available', ''))
        item = Item(**data)
        item.save()
        item_list_url = reverse_lazy('home')
        return HttpResponseRedirect(item_list_url)
    return render(request, 'items/item_create.html', context=data)