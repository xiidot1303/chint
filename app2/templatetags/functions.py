from django import template
from app2.models import Request as Request2
from functions.bot import *


register = template.Library()

@register.filter
def cuttext(text):
    if text:
        if len(text) > 14:
            r_text = text[:15] + '...'
        else:
            r_text = text
        return r_text
    else:
        return ''


@register.filter
def text_maker(obj):
    title = ' - Название: {}'.format(obj.title)
    description = ' - Описание: {}'.format(obj.description)
    point = ' - Баллы: {}'.format(obj.point)
    list_answers = [title, description, point]
    return list_answers

@register.filter
def overall_points(user):
    points = 0.0
    for r in Request2.objects.filter(user=user, status = 'conf'):
        points += r.point

    return points


@register.filter
def added_points(user):
    points = 0.0
    for r in Request2.objects.filter(user=user, status = 'conf'):
        points += r.point
    added = user.point2 + user.spent_for_prizes2 - points
    return added


@register.filter
def to_dict(f):
    print(f.__dict__)

@register.filter
def summ(a, b):
    return a + b

@register.filter
def number_for_string(n):
    n = str(int(n))
    n = n[::-1]
    r = ' '.join([n[i:i+3] for i in range(0, len(n), 3)])
    r = r[::-1]
    return r