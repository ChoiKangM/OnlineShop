from django.shortcuts import render, get_object_or_404

from .models import *

def product_in_category(request, category_slug=None):
    current_catetory = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_catetory = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_catetory)

    return render(request, 'shop/list.html',
                  {
                      'current_category': current_catetory,
                      'categories': categories,
                      'products': products
                  })
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    return render(request, 'shop/detail.html',
                  {
                      'product': product
                  })
