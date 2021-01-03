from django.db import models
from django.forms import ModelForm



from .models import Permit


class PermitForm(ModelForm):
    class Meta:
        model = Permit
        fields = [
            "permit_id",
            "requester_name",
            "requester_address",
            "requester_nid",
            "requester_contact_number",
            "start_date",
            "end_date",
            "request_reason",
            "permit_signer",
            "requester_location",
            ]
