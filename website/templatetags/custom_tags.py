# your_app/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Returns the value for the given key in the dictionary."""
    return dictionary.get(key)
