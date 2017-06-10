# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=20, blank=False, null=True)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=False, null=True)
    date_of_birth = models.DateTimeField(blank=False, null=True)
    mobile_number = models.CharField(max_length=20, blank=False, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    district = models.CharField(max_length=20, blank=False, null=True)
    city = models.CharField(max_length=20, blank=False, null=True)
    state = models.CharField(max_length=21, blank=False, null=True)
    country = models.CharField(max_length=21, blank=False, null=True)
    photo = models.ImageField(upload_to = 'images')
    verified = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=100, blank=True, null=True)
    #education_need = models.OneToOneField(educational_need)

    def __str__(self):
    	return self.user.username