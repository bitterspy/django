from django.template import Library

register = Library()

@register.filter(name='pub_date')
def pub_date(date):
    return date.year