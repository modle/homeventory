from django.shortcuts import render

from .models import Item


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'catalog/index.html', context)
