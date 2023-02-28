from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProductForm
from webapp.models import Products


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={'form': form})

    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_add.html', context={'form': form})
    else:
        Products.objects.create(**form.cleaned_data)
        return redirect('index')


def detail_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })


def update_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'image': product.image,
            'category': product.category,
            'remaining': product.remaining,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.category = form.cleaned_data['category']
            product.remaining = form.cleaned_data['remaining']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
        else:
            return render(request, 'product_update.html', context={'from': form, 'product': product})


def delete_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('index')


def cars_view(request):
    products = Products.objects.exclude(is_deleted=True).filter(category='Cars')
    context = {
        'products': products,
        'category': 'Cars'
    }
    return render(request, 'categories.html', context=context)


def alcohol_view(request):
    products = Products.objects.exclude(is_deleted=True).filter(category='Alcohol')
    context = {
        'products': products,
        'category': 'Alcohol'
    }
    return render(request, 'categories.html', context=context)


def smartphone_view(request):
    products = Products.objects.exclude(is_deleted=True).filter(category='Smartphone')
    context = {
        'products': products,
        'category': 'Smartphones'
    }
    return render(request, 'categories.html', context=context)


def other_view(request):
    products = Products.objects.exclude(is_deleted=True).filter(category='Other')
    context = {
        'products': products,
        'category': 'Other'
    }
    return render(request, 'categories.html', context=context)
