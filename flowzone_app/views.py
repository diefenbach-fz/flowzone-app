# django imports
from django.template import RequestContext


def invoice_customer(request, template_name="flowzone_app/invoice_customer.html"):
    return render_to_response(template_name, RequestContext(request, {}))
