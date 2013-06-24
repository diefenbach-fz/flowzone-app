# python imports
import requests

# django imports
from django.conf import settings
from django.template import Library
from django.utils.safestring import mark_safe

# lfs imports
from lfs.catalog.models import Product

# flowzone_app imports
import flowzone_app.views
from lfs_ustore import UStore

register = Library()

@register.simple_tag(takes_context=True)
def invoice_customer(context, customer_id):
    request = context.get("request")
    result = flowzone_app.views.invoice_customer(request, customer_id)
    return mark_safe(result)

@register.simple_tag(takes_context=True)
def ustore_link(context, product_id):
    request = context.get("request")

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return ""

    if not product.external_id:
        return ""

    email = request.session.session_key + "@srz.de"

    # Create ustore user if necessary
    ustore = UStore(request)
    if ustore.get_user(email) is None:
        user_id = ustore.add_user(email)
        ustore.add_user_to_group(user_id, getattr(settings, "USTORE_GROUP"))

    url = ustore.get_single_signon_url_to_product_details(email, product.external_id)
    return mark_safe(url)
