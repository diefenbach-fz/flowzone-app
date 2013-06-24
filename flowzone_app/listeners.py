# django imports
from django.dispatch import receiver

# lfs imports
from lfs.core.signals import order_submitted
from lfs.core.signals import order_paid

# ustore imports
from lfs_ustore import UStore


@receiver(order_paid)
def submit_order_to_ustore(sender, **kwargs):
    order = sender.get("order")
    request = sender.get("request")

    item = order.items.all()[0]

    order_id, order_product_id = item.external_id.split("/")
    order_id = order_id.strip()
    order_product_id = order_product_id.strip()

    ustore = UStore(request)
    ustore.submit_order(order_id)
