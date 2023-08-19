from django.contrib import admin
from .models import *
# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display =[

    ]



class TagAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
        'title',
        'is_active',
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
        'title',
        'is_active',
    ]

class PricingAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
        'title',
        'is_active',
    ]

admin.site.register(Product,ProductAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Pricing,PricingAdmin)







