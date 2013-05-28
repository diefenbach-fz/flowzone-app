# django imports
from django.template import Library
from django.utils.safestring import mark_safe

# flowzone_app imports
from flowzone_app.views import invoice_customer

register = Library()


@register.simple_tag(takes_context=True)
def invoice_customer(context, obj):
    request = context.get('request', None)
    result = invoice_customer(request)
    return mark_safe(result)
