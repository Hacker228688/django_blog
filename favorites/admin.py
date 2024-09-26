from django.contrib import admin
from .models import Favorite, FavoritesItem

class FavoritesItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'favorite', 'quantity', 'total_price_field',)
    search_fields = ('item__title', 'favorite__user__username',)
    list_filter = ('item', 'favorite__user',)
    raw_id_fields = ('item', 'favorite',)

    def total_price_field(self, obj):
        return obj.total_price

    total_price_field.short_description = 'Общая цена'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'favorites_items',)
    search_fields = ('user__username', 'user__email', 'created_at',)
    readonly_fields = ('total_price',)

    def favorites_items(self, obj):
        return [o for o in obj.favoritesitem_set.all()]

    favorites_items.short_description = 'Список товаров'


admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(FavoritesItem, FavoritesItemAdmin)

