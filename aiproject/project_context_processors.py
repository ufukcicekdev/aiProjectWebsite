from aiwebsite.models import Category,Pricing


def global_category_context(reequest):
    return dict(
        global_categories = Category.objects.filter(is_active=True)
    )

def global_pricing_context(reequest):
    return dict(
        global_pricing = Pricing.objects.filter(is_active=True)
    )
