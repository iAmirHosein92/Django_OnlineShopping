from django.db import models
from django.urls import reverse

class Category(models.Model):
    sub_category = models.ForeignKey('self', related_name='scategory', null=True, on_delete=models.CASCADE, blank=True )
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products', blank=True )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField()
    description = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail', kwargs={'slug': self.slug})

