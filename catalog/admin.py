from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    fields = ['item_name', 'item_location']

admin.site.register(Item)
