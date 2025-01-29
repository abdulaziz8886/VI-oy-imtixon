from django import template
from app.models import categorygander, categoryProduct, categorySale

register = template.Library()


@register.simple_tag(name='categories')
def get_categories():
    return categorygander.objects.all()


@register.simple_tag(name='categories1')
def get_categories():
    return categorySale.objects.all()

@register.simple_tag(name='category2')
def get_categories():
    return categoryProduct.objects.all()
