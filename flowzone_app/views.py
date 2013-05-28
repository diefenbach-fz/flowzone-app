# django imports
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.customer.models import Customer
from lfs.core.utils import MessageHttpResponseRedirect

# flowzone_app imports
from flowzone_app.forms import CustomerForm


def invoice_customer(request, customer_id, template_name="flowzone_app/invoice_customer.html"):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return HttpResponseRedirect(reverse("lfs_manage_customer", kwargs={"customer_id": customer_id}))

    form = CustomerForm(initial={"allow_invoice": customer.allow_invoice})

    if request.method == "POST":
        if request.POST.get("allow_invoice"):
            customer.allow_invoice = True
        else:
            customer.allow_invoice = False
        customer.save()

        return MessageHttpResponseRedirect(
            redirect_to=reverse("lfs_manage_customer", kwargs={"customer_id": customer_id}),
            msg=_(u"The customer has been modified."))
    else:
        return render_to_string(template_name, RequestContext(request, {
            "form": form,
            "customer_id": customer_id,
        }))
