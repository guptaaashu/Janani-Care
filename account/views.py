# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import datetime
import hashlib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from account.models import UserProfile
from account.forms import RegistrationForm



def send_email(user, profile):
    email_subject = 'New account confirmation'
    email_body = "Hello, %s,\n\n\
        Thank you for signing up to Janani care! To activate your account, \
        click this link within 24 hours:\n\
        http://localhost:8000/confirm?q=%s" % (
            user.first_name, profile.activation_key)
    send_mail(email_subject, email_body, settings.EMAIL_HOST, [user.email])


def signup(request):
    if not request.user.is_authenticated():
        form = RegistrationForm() 
        if request.method == 'POST':
            form = RegistrationForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                activation_key = (hashlib.sha224(user.username.encode('utf-8'))
                    .hexdigest())
                profile = UserProfile(user=user, activation_key=activation_key)
                profile.save()
                send_email(user, profile)
                messages.info(request, 'Check email for a confirmation link!')
                return redirect('/')          
        return render(request, 'signup.html', {'form': form})
    return redirect('/kkk')


def confirm(request):
    activation_key = request.GET.get('q', '')
    profile = get_object_or_404(UserProfile, activation_key=activation_key)
    user = profile.user
    user.verified = True
    user.save()
    return render(request, 'confirm.html', {'success': True})