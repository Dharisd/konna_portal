from django.db import models
import datetime
from django.utils.timezone import now
from django.urls import reverse


class Signers(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)


    def __str__(self):
        return self.name




class Permit(models.Model):
    #can implement the logic for this later
    permit_id = models.CharField(max_length=200 )

    requester_name = models.CharField(max_length=200)
    requester_address = models.CharField(max_length=200)
    requester_nid = models.CharField(max_length=200)
    requester_contact_number = models.PositiveIntegerField()
    requester_date = models.DateField(default=now)
    requester_location = models.CharField(max_length=500)
    #working and ending dates
    start_date = models.DateField()
    end_date = models.DateField(default=None, blank=True,null=True)
    #reason
    INTERNET = 'NET'
    CURRENT = 'CURRENT'
    TV = 'TV'
    OTHER = 'OTHER'
    REQUEST_REASON_TYPES = [
        (INTERNET, 'INTERNET'),
        (CURRENT, 'CURRENT'),
        (TV, 'TV'),
        (OTHER, 'OTHER'),
    ]
    request_reason = models.CharField(
        max_length=10,
        choices=REQUEST_REASON_TYPES,
        default=CURRENT)
    permit_signer = models.ForeignKey(Signers,on_delete=models.CASCADE)

    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.permit_id

    def get_absolute_url(self):
        return reverse('dig_permit:details', args=[str(self.pk)])

