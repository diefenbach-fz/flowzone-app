# django imports
from django.template import Library
from django.utils.safestring import mark_safe

# flowzone_app imports
import flowzone_app.views

register = Library()


@register.simple_tag(takes_context=True)
def invoice_customer(context, customer_id):
    request = context.get("request")
    result = flowzone_app.views.invoice_customer(request, customer_id)
    return mark_safe(result)
