# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Envoice(models.Model):

    #__Envoice_FIELDS__
    invoiceid = models.CharField(max_length=255, null=True, blank=True)
    sellerid = models.CharField(max_length=255, null=True, blank=True)
    buyerid = models.CharField(max_length=255, null=True, blank=True)
    customerid = models.CharField(max_length=255, null=True, blank=True)
    deviceid = models.CharField(max_length=255, null=True, blank=True)
    payment_methodid = models.CharField(max_length=255, null=True, blank=True)
    cancelreasonid = models.IntegerField(null=True, blank=True)
    errortypeid = models.IntegerField(null=True, blank=True)
    productname = models.TextField(max_length=255, null=True, blank=True)
    city = models.TextField(max_length=255, null=True, blank=True)
    subtotal_amount = models.CharField(max_length=255, null=True, blank=True)
    tax_amount = models.CharField(max_length=255, null=True, blank=True)
    discount_amount = models.CharField(max_length=255, null=True, blank=True)
    totalamount = models.CharField(max_length=255, null=True, blank=True)
    invoice_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    paymentdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Envoice_FIELDS__END

    class Meta:
        verbose_name        = _("Envoice")
        verbose_name_plural = _("Envoice")



#__MODELS__END
