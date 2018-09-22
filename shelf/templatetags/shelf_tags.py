from django.template import Library

register = Library()

@register.filter(name='pub_date')
def pub_date(date):
    return date.year

# wyświetl edycje korzystając z szablonu show_editions
@register.inclusion_tag('tags/show_editions.html')
def show_editions(obj):
    return {'editions': obj.editions.all()}