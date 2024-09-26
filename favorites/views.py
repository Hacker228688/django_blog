from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from store.models import Item
from .models import Favorite, FavoritesItem


@login_required
def favorite(request):

    favorite = Favorite.objects.filter(user=request.user).first()

    if not favorite:
        favorite = Favorite.objects.create(user=request.user)

    context = {
        'favorite_items': FavoritesItem.objects.filter(favorite=favorite),
        'favorite': favorite
    }

    return render(request, 'favorites/favorites.html', context)


@login_required
def add_to_favorite(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    favorite, _ = Favorite.objects.get_or_create(user=request.user)

    favorites_item, created = FavoritesItem.objects.get_or_create(
        favorite=favorite,
        item=item
    )

    if created:
        print(f"Товар {item.title} добавлен в избранное.")
    else:
        print(f"Товар {item.title} уже в избранном, Увеличиваем корличество.")

        favorites_item.quantity += 1

    return redirect('favorites:favorites')


@login_required
def delete_favorite_item(request, item_slug):

    cart_item = FavoritesItem.objects.get(
        favorite=Favorite.objects.get(user=request.user),
        item=get_object_or_404(Item, slug=item_slug)
    )
    cart_item.delete()
    return redirect('favorites:favorites')


@login_required
def update_cart_item(request):

    if request.method == 'POST' and request.is_ajax():
        favorites_item_id = request.POST.get('favorites_item_id')
        new_quantity = int(request.POST.get('new_quantity'))
        favorites_id = int(request.POST.get('favorites_id'))

        favorites = Favorite.objects.get(pk=favorites_id)
        favorites_item = get_object_or_404(FavoritesItem, id=favorites_item_id)
        favorites_item.quantity = new_quantity
        favorites_item.save()
        return JsonResponse({
            'success': True,
            'favorites_item_id': favorites_item.id,
            'favorites_item_quantity': favorites_item.quantity,
            'favorites_total_count': favorites_item.total_count,
            'favorites_total_price': favorites.total_price
        })
    else:
        return JsonResponse({
            'success': False, 'error': 'Invalid request method'
        })

