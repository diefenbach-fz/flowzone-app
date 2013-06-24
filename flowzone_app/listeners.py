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

    for item in order.items.all():
        if item.external_order_id:
            ustore = UStore(request)
            ustore.submit_order(item.external_order_id)
            break
