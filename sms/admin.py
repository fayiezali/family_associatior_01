from django.contrib import admin
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
# from sms.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
# 
from django.contrib.admin.decorators import display
# from .models import PreRegistration
# # Register your models here.
# @admin.register(PreRegistration)
# class PreRegistrationAdmin(admin.ModelAdmin):
#     list_display=['first_name','last_name']
































# # Send Message
# @admin.register(SendMessagesMODEL)
# class SendMessagesADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
#         #
#         # Add aFilter Box
#         list_filter = (
#         'SM_SubscriptionAmount',
#         )
#         #
#         #
#         # Show Fields a List
#         list_display = (
#         'SM_SubscriptionAmount', 
#         )
#         #
#         # search list
#         search_fields = ['SM_SubscriptionAmount']

#         # inlines = [PersonalDataInline]