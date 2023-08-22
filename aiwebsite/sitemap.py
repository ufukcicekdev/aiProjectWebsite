from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .models import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

startdate = datetime.today()
enddate = startdate + relativedelta(years=10)



class CategoryLinkSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Category.objects.filter(is_active=True)

    def location(self,obj):
        return f"/category/{obj.slug}"
    
class PricingLinkSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Pricing.objects.filter(is_active=True)

    def location(self,obj):
        return f"/pricing/{obj.slug}"