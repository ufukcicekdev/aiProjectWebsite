from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#Third Party Apps:
from autoslug import AutoSlugField



class Pricing(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = 'title', unique = True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'pricing_view',
            kwargs={
                'pricing_slug':self.slug
            }
        )


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = 'title', unique = True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'category_view',
            kwargs={
                'category_slug':self.slug
            }
        )



class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = 'title', unique = True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'tag_view',
            kwargs={
                'tag_slug':self.slug
            }
        )



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = AutoSlugField(populate_from = 'title', unique = True)
    pricingModel = models.ForeignKey(Pricing,on_delete=models.SET_NULL,null=True)
    tooltags = models.ManyToManyField(Tag)
    url = models.TextField(blank=True, null=True)
    imageSrc = models.TextField(blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse(
            'product_detail_view',
            kwargs={
                'category_slug':self.category.slug,
                'product_slug':self.slug
            }
        )