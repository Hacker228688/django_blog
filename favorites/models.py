from django.db import models
from django.contrib.auth.models import User
from django.db import models

from store.models import Item


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites_list',
        verbose_name='Покупатель',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания',)

    class Meta:
        verbose_name = 'Избранное'


    @property
    def total_price(self):
        total_price = sum(item.total_price for item in self.items.all())
        return total_price

    def __str__(self):
        return f"Favorite {self.id} for {self.user.username}"

    def clear(self):
        self.items.all().delete()


class FavoritesItem(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Избранное',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество',)

    class Meta:
        verbose_name = 'Товары в избранное'


    @property
    def total_price(self):
        total_price = self.quantity * self.item.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.item.title}"


