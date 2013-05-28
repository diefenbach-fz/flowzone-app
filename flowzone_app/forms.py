# django imports
from django import forms
from django.utils.translation import ugettext_lazy as _


class CustomerForm(forms.Form):
    allow_invoice = forms.BooleanField(label=_(u"Allow invoice"))
