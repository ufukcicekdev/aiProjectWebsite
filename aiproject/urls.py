"""
URL configuration for aiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from aiwebsite.sitemap import CategoryLinkSiteMap,PricingLinkSiteMap
from django.urls import re_path
from django.views.generic import TemplateView
from aiwebsite.views import (
    home_view,
    category_view,
    product_detail_view,
    pricing_view,
    search_view
)

sitemaps = {
    'categoryLinkSiteMap':CategoryLinkSiteMap, 
    'pricingLinkSiteMap':PricingLinkSiteMap,   
}

app_name = "aiwebsite"

urlpatterns = [
    path('',home_view,name='home'),
    path('category/<slug:category_slug>/',category_view, name = "category_view"),
    path('pricing/<slug:pricing_slug>/',pricing_view, name = "pricing_view"),
    path('search/',search_view, name = "search_view"),
    path('category/<slug:category_slug>/product/<slug:product_slug>/',product_detail_view, name = "product_detail_view"),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
]
