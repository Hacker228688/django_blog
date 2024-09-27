from django.urls import path
from .views import favorite, add_to_favorite, delete_favorite_item, update_cart_item

app_name = 'favorites'

urlpatterns = [
    path('', favorite, name='favorites'),
    path('add_favorites/<slug:item_slug>/', add_to_favorite, name='add_to_favorite'),
    path('delete_favorites/<slug:item_slug>/', delete_favorite_item, name='delete_favorite_item'),
    path('update_favorites/', update_cart_item, name='update_favorites')
]