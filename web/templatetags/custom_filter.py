from django import template

register = template.Library()
@register.filter
def rating_star(arg, value):
    new =""
    for i in range(int(arg)):
        new = new + value
    return new