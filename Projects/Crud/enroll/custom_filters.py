# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def mask_password(password):
    return '******'  # Or return '*' * len(password)
