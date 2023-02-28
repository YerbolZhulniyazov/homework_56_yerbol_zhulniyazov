from django.contrib import admin
from webapp.models import Products


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'remaining', 'price', 'image', 'is_deleted', 'deleted_at')
    list_filter = ('id', 'name', 'category', 'price', 'remaining', 'is_deleted', 'deleted_at')
    search_fields = ('id', 'category', 'description', 'remaining', 'price')
    fields = ('id', 'name', 'category', 'description', 'price', 'remaining', 'image')
    readonly_fields = ('id',)


admin.site.register(Products, ProductAdmin)
