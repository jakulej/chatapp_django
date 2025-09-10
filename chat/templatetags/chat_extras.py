from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@stringfilter
def userchar(value):
    userchar = value[:1]
    userchar = userchar.upper()
    return userchar


register.filter("userchar", userchar)
