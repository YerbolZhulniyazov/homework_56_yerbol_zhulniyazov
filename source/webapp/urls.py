from django.urls import path

from webapp.views.base import index_view
from webapp.views.products import add_view, detail_view, update_view, delete_view, confirm_delete, \
    alcohol_view, cars_view, smartphone_view, other_view

urlpatterns = [
    path("", index_view, name='index'),
    path("products/", index_view),
    path('product/add', add_view, name='product_add'),
    path('product/<int:pk>', detail_view, name='detail_product'),
    path('product/<int:pk>/update/', update_view, name='product_update'),
    path('product/<int:pk>/delete/', delete_view, name='product_delete'),
    path('product/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete'),
    path('products/cars/', cars_view, name='cars_view'),
    path('products/alcohol/', alcohol_view, name='alcohol_view'),
    path('products/smartphone/', smartphone_view, name='smartphone_view'),
    path('products/other/', other_view, name='other_view')
]
