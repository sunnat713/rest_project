from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db.models import Q
import random

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']


class ProductQuerySet(models.QuerySet):
    def is_pubic(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_pubic().filter(lookup)
        if user is not None:
            qs2 = qs.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=150, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    # objects = ProductManager()
    @property
    def path(self):
        return f'/product/{self.pk}/'

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    @property
    def body(self):
        return self.content

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"

    def is_public(self) -> bool:
        return self.public
