from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Products


def index_view(request: WSGIRequest):
    products = Products.objects.exclude(is_deleted=True).order_by('category', 'name')
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)
