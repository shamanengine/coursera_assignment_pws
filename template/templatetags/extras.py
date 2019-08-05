from django import template

register = template.Library()


@register.filter(name='inc')
def inc(value, arg):
    """Фильтр “inc“ который принимает 2 аргумента:
    1-й - число которое нужно увеличить,
    2-й - на сколько нужно увеличить первое число.
    """
    return int(value) + int(arg)


@register.simple_tag
def division(a, b, to_int=False):
    """Тег “division“ (то есть тег для деления), который принимает 3 аргумента:
    1-й - делимое, 2-й - делитель, 3-й - деление целочисленное (именованный аргумент to_int).
    По умолчанию необходимо сделать вещественное деление.
    Обратите внимание, что делимое и делитель целые числа, но передается в тег в формате string.
    """
    if to_int and abs(int(b)) > abs(int(a)) and int(a) * int(b) < 0:
        return 0

    return int(a) // int(b) if to_int else int(a) / int(b)
