from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorite, name='favorites'),
    path('add/<slug:item_slug>/', views.add_to_favorite, name='add_to_favorite'),
    path('delete/<slug:item_slug>/', views.delete_favorite_item, name='delete_favorite_item'),
    path('update/', views.update_cart_item, name='update_favorites')
]