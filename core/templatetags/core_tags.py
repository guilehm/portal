from django import template

from register.models import MainCompany
from utils.weather import icon_dict

register = template.Library()


@register.inclusion_tag('core/tags/logo_tag.html')
def logo_tag():
    company = MainCompany.objects.first()
    return {'logo': company.logo}


@register.inclusion_tag('core/tags/logo_mini_tag.html')
def logo_mini_tag():
    company = MainCompany.objects.first()
    return {'logo': company.logo_thumb}


@register.filter(name='get_icon')
def get_icon(code):
    return icon_dict.get(code)


@register.filter(name='f_to_c')
def fahrenheit_to_celsius(temperature_f):
    return (float(temperature_f) - 32) / 1.8
