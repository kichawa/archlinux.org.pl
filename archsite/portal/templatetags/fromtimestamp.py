from django import template
from datetime import datetime
import bbcode

register = template.Library()

@register.filter
def todate(value):
    date = datetime.fromtimestamp(value)
    return date


@register.filter
def bbcode2html(value):
    return bbcode.render_html(value)
