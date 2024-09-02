from django.contrib import admin
from .models import Item


class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status', )
    search_fields = ('meals', 'description')

admin.site.register(Item, MenuItemsAdmin)