from http import server
import smtplib
from django.db import models
#
from typing import ClassVar
#
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
from django.urls import reverse  # To generate URLS by reversing URL patterns
#
from django.db.models.signals import post_save # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده
#
from django.utils.text import slugify
#
from datetime import datetime
#
from datetime import date
#
from twilio.rest import Client
#
import os
from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS
#
import django
from django.shortcuts import render #
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.auth import  get_user_model #
from django.contrib.auth.views import TemplateView #
# from django.views import View #
# from accounts.forms import SignUpForm #
from django.template.loader import render_to_string #
from django.contrib.sites.shortcuts import get_current_site #
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode #
from django.utils.encoding import force_bytes #
from django.contrib.auth.tokens import default_token_generator #
from django.core.mail import EmailMessage #
from django.contrib import messages
from django.utils import timezone
from django.views.generic import TemplateView , ListView ,DetailView , DeleteView, UpdateView  , FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy , reverse
from django.db.models import Q # new
from django.http import JsonResponse
from django.contrib import messages
# from accounts.models import PersonalsMODEL , FinancialStatementsMODEL , DatesReceivingMoneyPaymentsMODEL
# UserModel = get_user_model()
import pywhatkit as pwt # Send messages To WhatsApp
import random
#
import pywhatkit as pwk
#
from django.core.mail import send_mail
# from django.core.mail import send_mail
# from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS
#
# from django.db.models.signals import post_save , post_delete # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده
#
from django.dispatch import receiver


# Create your models here.
# class PreRegistration(models.Model):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password1 = models.CharField(max_length=100)
#     password2 = models.CharField(max_length=100)
#     otp = models.CharField(max_length=10)




















# # (1)Personal Data
# class SendMessagesMODEL(models.Model):
# #
#     # SM_User                   = models.OneToOneField(User                         , on_delete=models.CASCADE                 , verbose_name="اسم المشترك")
#     SM_SubscriptionAmount     = models.DecimalField(default=50 , max_digits=8 , decimal_places=2                  , db_index=True , blank=False  , null=False , verbose_name="مبلغ الإشتراك")
#     SM_Email                  = models.EmailField(default='fayiez@outlook.com')
#     SM_Mobil                  = models.CharField(default='+0000000000' ,max_length=17 , db_index=True , blank=False  , null=False , verbose_name="الجوال")
# #
#     # Send OTP 
# @receiver(post_save,sender=User)
# def send_message_to_whatsapp(sender,instance,created,**kwargs):
#     # [TWILIO_ACCOUNT_SID]Account SID From Twilio
#     account_sid = 'ACd5219db82f4052208e4e57b1397e9b71'
#     # [TWILIO_AUTH_TOKEN]Auth Token From Twilio            
#     auth_token  = '887741e7416254b52737f6d2b71a903a'
#     client      = Client(account_sid, auth_token)
#     messages     = client.messages.create(
#             media_url=["https://duckduckgo.com/?q=flor.png&atb=v329-1&iar=images&iax=images&ia=images&iai=https%3A%2F%2Fwww.pngpix.com%2Fwp-content%2Fuploads%2F2016%2F03%2FDahlia-Flower-PNG-image.png"],
#             from_='+19794736580',
#             body=f"Family Associatior - Hi there The Curent Result Is - ",  
#             to='+0000000000')
#     print('Messages Whatsapp Sended')
#         # else:
        
        #                 # [TWILIO_ACCOUNT_SID]Account SID From Twilio
        #     account_sid = 'AC9c97dcf191d694b3bc982ea3b8959d43'
        #     # [TWILIO_AUTH_TOKEN]Auth Token From Twilio            
        #     auth_token  = '2530aeed15bee9ea8601c2ee421c6916'
        #     client      = Client(account_sid, auth_token)

        #     message = client.messages.create(body=f"Family Associatior - Hi there The Curent Result Is - {self.SM_SubscriptionAmount}", from_='+19804476399',to='+0000000000')

    # print(message.sid)
    # return super().save(*args , **kwargs)
