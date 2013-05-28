# django imports
from django.conf.urls.defaults import *


urlpatterns = patterns('flowzone_app.views',
    url(r'^invoice-customer/(?P<customer_id>\d*)$', "invoice_customer", name="lfs_invoice_customer"),
)
