from django import template
import datetime
from django.template.loader import render_to_string

from Blog.models import Category

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag('category.html')
def show_category():
    categrories = Category.objects.all()[0:8]
    return {'categories': categrories}