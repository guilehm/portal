from django import template

from register.models import MainCompany

register = template.Library()


@register.inclusion_tag('core/tags/logo_tag.html')
def logo_tag():
    company = MainCompany.objects.first()
    return {'logo': company.logo}


@register.inclusion_tag('core/tags/logo_mini_tag.html')
def logo_mini_tag():
    company = MainCompany.objects.first()
    return {'logo': company.logo_thumb}
