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
from django.views import View #
from accounts.forms import SignUpForm #
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
from accounts.models import PersonalsMODEL , FinancialStatementsMODEL , DatesReceivingMoneyPaymentsMODEL
UserModel = get_user_model()
import pywhatkit as pwt # Send messages To WhatsApp
import random
#
#
from django.core.mail import send_mail
# from django.core.mail import send_mail
from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS
#

# (1)Personal Data
class SendMessagesMODEL(models.Model):
#
    # SM_User                   = models.OneToOneField(User                         , on_delete=models.CASCADE                 , verbose_name="اسم المشترك")
    SM_SubscriptionAmount     = models.DecimalField(default=50 , max_digits=8 , decimal_places=2                  , db_index=True , blank=False  , null=False , verbose_name="مبلغ الإشتراك")
    SM_Email                  = models.EmailField()
#
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.SM_SubscriptionAmount)
    # Send Email 
    def save(self , *args , **kwargs):
        user = User.objects.get(id=11)
        SendTo = user.email
        print(SendTo)
        if self.SM_SubscriptionAmount < 50:
            send_mail(
            'Family Association',
            'Thank you for joining the family association.',
            EMAIL_HOST_USER,
            [SendTo],
            fail_silently=False,
        )
#     # Auto Save Slug 
#     def save(self , *args , **kwargs):
#         if self.SM_SubscriptionAmount < 50:
#             # [TWILIO_ACCOUNT_SID]Account SID From Twilio
#             account_sid = '000000000000'
#             # [TWILIO_AUTH_TOKEN]Auth Token From Twilio            
#             auth_token  = '000000000000'
#             client      = Client(account_sid, auth_token)
        
#             message = client.messages.create(body=f"Family Associatior - Hi there The Curent Result Is - {self.SM_SubscriptionAmount}", from_='+000000000000',to='+000000000000')
#         else:
#                         # [TWILIO_ACCOUNT_SID]Account SID From Twilio
#             account_sid = 'AC9c97dcf191d694b3bc982ea3b8959d43'
#             # [TWILIO_AUTH_TOKEN]Auth Token From Twilio            
#             auth_token  = '2530aeed15bee9ea8601c2ee421c6916'
#             client      = Client(account_sid, auth_token)
        
#             message = client.messages.create(body=f"Family Associatior - Hi there The Curent Result Is - {self.SM_SubscriptionAmount}", from_='+000000000000',to='+000000000000')

#             print(message.sid)
#         return super().save(*args , **kwargs)


# #
#     def save(self , *args , **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.P_User.username)
#         super(PersonalsMODEL , self).save(*args , **kwargs)

#     def save(self , *args , **kwargs):
#         if self.SM_SubscriptionAmount < 50:
#         # if not self.SM_SubscriptionAmount:
#             server=smtplib.SMTP('smtp.gmail.com',587)
#             server.starttls()
#             server.login('family00associatior@gmail.com','ckvtsgoimjepbriu')
#             msg=("Thank you for joining the family association")
#             server.sendmail('family00associatior@gmail.com','fayiez@outlook.com',msg)
#             server.quit()
#         return super().save(*args , **kwargs)
    
    
#     def save(self , *args , **kwargs):
#         if self.SM_SubscriptionAmount < 50:
#             server=smtplib.SMTP('smtp.gmail.com',587)
#             server.starttls()
#             server.login('family00associatior@gmail.com','ckvtsgoimjepbriu')
#             msg=("Thank you for joining the family association")
#             subject =("fayez")
#             server.sendmail('family00associatior@gmail.com','fayiez@outlook.com',msg,subject)
#             server.quit()
#         return super().save(*args , **kwargs)



# from django.core.mail import send_mail
# from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS

# send_mail('Family Association','Thank You For Joining The Family Association',  None,  ['fayiez@outlook.com'],  fail_silently=False,)

#     def save(self , *args , **kwargs):
#         if self.SM_SubscriptionAmount < 50:
#             send_mail(
#             'Family Association',
#             'Thank you for joining the family association.',
#             EMAIL_HOST_USER,
#             ['fayiez@outlook.com'],
#             fail_silently=False,
#         )