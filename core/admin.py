from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.News)
admin.site.register(models.Xiomi)
admin.site.register(models.Phone)
admin.site.register(models.PhoneCategory)
admin.site.register(models.PhoneColor)
admin.site.register(models.Products)
admin.site.register(models.ProductsAttribute)
admin.site.register(models.ProductsClass)
admin.site.register(models.Users)
admin.site.register(models.Sides)

