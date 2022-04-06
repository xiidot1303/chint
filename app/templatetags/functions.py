from django import template
from app.models import *
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
    for r in Request.objects.filter(user=user, status = 'conf'):
        points += r.point

    return points