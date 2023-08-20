from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.



def home_view(request):
    items_per_page = 12
    products = Product.objects.filter(is_active=True)
    paginator = Paginator(products, items_per_page)

    page_number = request.GET.get('page')  # URL'den sayfa numarasını alın
    
    page_obj = paginator.get_page(page_number) 

    context = dict(
        products = products,
        page_obj =page_obj
    )
    return render(request, 'page/product_list.html',context)


def search_view(request):
    query = request.GET.get('q')
    if query:
        query = Product.objects.filter(Q(title__icontains=query) | Q(Description__icontains=query))
    
    context = dict(
        query = query
    )
    return render(request, 'page/product_list.html',context)




def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(is_active=True, category = category)
    context = dict(
        category = category,
        products = products,
    )  
    return render(request , 'page/product_list.html', context)


def pricing_view(request, pricing_slug):
    pricing = get_object_or_404(Pricing, slug=pricing_slug)
    products = Product.objects.filter(is_active=True, pricingModel = pricing)
    context = dict(
        pricing = pricing,
        products = products,
    )  
    return render(request , 'page/product_list.html', context)


def product_detail_view(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    context = dict(
        product = product
    )
    return render(request, 'page/product_detail.html',context)