from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


# Create your models here.

class ProductsChoice(TextChoices):
    ALCOHOL = 'Alcohol', 'Алкоголь'
    SMARTPHONE = 'Smartphone', 'Смартфон'
    CARS = 'Cars', 'Машины'
    OTHER = 'Other', 'Разное'


class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=False, verbose_name='Описание товара')
    image = models.CharField(max_length=300, null=False, blank=False, verbose_name='Фото')
    category = models.CharField(choices=ProductsChoice.choices, default=ProductsChoice.OTHER, max_length=60,
                                verbose_name='Категория')
    remaining = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f'{self.name} - {self.description} - {self.category}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
