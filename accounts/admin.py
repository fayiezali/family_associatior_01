from django.contrib import admin
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from accounts.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
# 
#
# 
# 
# 
# 
"""Important Note:
(fields) & (fieldsets) This Properties Can Not Be Put Together
# Controlling Which fields are Displayed and Laid Out
# fields = [('ASS_NameAssociation', 'ASS_Slug' ), 'ASS_AssociationLogo' , 'ASS_Address' ,('ASS_Mobile' , 'ASS_Phone') , 'ASS_Email' , 'ASS_BankAccount']
"""
#
#
#
#
##########################################################################
# *** Add The Child Table Inside The Parent Table ***
# class FinancialDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = FinancialData_MODEL
# #
# class HousingDataDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = HousingData_MODEL
#
# class PersonalDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = PersonalData_MODEL
##########################################################################
#
# Personal File
@admin.register(PersonalFile_MODEL)
class PersonalFile_ADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        # Automatically Fill In Slug Field From Variable (FullName)
        FullName = {
        "PF_Slug": # Slug Field
        [
        'PF_FirstName'       , 
        'PF_FatherName'      ,
        'PF_GrandFatherName' ,
        'PF_FamilyName'
        ]
        } # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
        prepopulated_fields = FullName
        #
        #
        # Add a Filter Box
        list_filter = (
        'PF_User'     , 
        'PF_Mobile'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'PF_User'                  , 
        'PF_Slug'                  ,
        'PF_Avialable'             , 
        'PF_FirstName'             ,
        'PF_FatherName'            ,
        'PF_GrandFatherName'       ,
        'PF_FamilyName'            ,
        'PF_Photo'                 ,
        'PF_Mobile'                ,
        'PF_Address'               ,
        'PF_Notes'
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, 
        {
        'fields': (
        'PF_User'              ,
        'PF_Slug'              ,
        'PF_Avialable'         ,
        'PF_FirstName'         ,
        'PF_FatherName'        ,
        'PF_GrandFatherName'   ,
        'PF_FamilyName'        ,
        'PF_Address'           
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',),
        'fields': (
        'PF_Photo'            ,
        'PF_Notes'    
        )
        }
        ),
        )
# 
# Financial Statements
@admin.register(FinancialStatements_MODEL)
class FinancialStatements_ADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add aFilter Box
        list_filter = (
        'FS_User'                  , 
        'FS_BankAccount'           , 
        'FS_SubscriptionAmount'    ,
        'FS_NumberPaymentsDue'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'FS_User'                   , 
        'FS_SubscriptionAmount'     , 
        'FS_NumberPaymentsDue'      , 
        'FS_BankName'               , 
        'FS_BankAccount'            , 
        'FS_Notes'
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'FS_User'                      , 
        'FS_SubscriptionAmount'                , 
        'FS_NumberPaymentsDue'              , 
        'FS_BankName'                  ,  
        'FS_BankAccount'               
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',)    ,
        'fields': (
        'FS_Notes' ,
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
# 
# 
# 
# Dates Receiving Payments
@admin.register(DatesReceivingPayments_MODEL)
class DatesReceivingPayments_ADMIN(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add aFilter Box
        list_filter = (
        'DRP_User'      , 
        'DRP_DateReceivigPayments_Long'   ,
        'DRP_DateReceivigPayments_Short'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'DRP_User'     , 
        'DRP_DateReceivigPayments_Long'   , 
        'DRP_DateReceivigPayments_Short'  , 
        'DRP_Notes'
        )
        #
        # search list
        search_fields = ['DRP_DateReceivigPayments_Long']
    
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'DRP_User'                        , 
        'DRP_DateReceivigPayments_Long'   , 
        'DRP_DateReceivigPayments_Short'  
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',) ,
        'fields': (
        'DRP_Notes',
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
# 
#


























































































# # Comprehensive Record
# @admin.register(Association_Months_MODEL)
# class Association_Months_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
#         #
#         # Add aFilter Box
#         list_filter = (
#         # 'AM_MonthNumber'       , 
#         'AM_MonthName'         , 
#         'AM_User'              ,
#         'AM_DateShareReceived' ,
#         # 'AM_ShareValue'        ,
#         'AM_NumberShares'      ,
#         'AM_DeservedAmount'    ,
#         # 'AM_Notes'
#         )
#         #
#         #
#         # Show Fields a List
#         list_display = (
#         'AM_MonthName'         , 
#         'AM_User'              ,
#         'AM_DateShareReceived' ,
#         'AM_ShareValue'        ,
#         'AM_NumberShares'      ,
#         'AM_DeservedAmount'    ,
#         'AM_Notes'
#         )
#         #
#         # search list
#         search_fields = ['AM_MonthName']
#         #
#         #
#         # Add Data In Different Sections
#         fieldsets = (
#         (None, {
#         'fields': (
#         # 'AM_MonthNumber'       , 
#         'AM_MonthName'         , 
#         'AM_User'              ,
#         'AM_DateShareReceived' ,
#         'AM_ShareValue'        ,
#         'AM_NumberShares'      ,
#         'AM_DeservedAmount'    ,
#         )
#         }
#         ),
#         ('Advanced', {
#         'classes': ('collapse',) ,
#         'fields': (
#         'AM_Notes',
#         )
#         }
#         ),
#         )
#         # inlines = [PersonalDataInline]
# # 
# # 
# # 
# # Monthes_List
# @admin.register(Monthes_Menu_MODEL)
# class Monthes_Menu_MODEL_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
#         #
#         # Add aFilter Box
#         list_filter = (
#         'MM_MonthName'      ,
#         )
#         #
#         #
#         # Show Fields a List
#         list_display = (
#         # 'AM_MonthNumber'       , 
#         'MM_MonthName'      , 
#         )
#         #
#         # search list
#         search_fields = ['MM_MonthName']
#         #
#         #
#
#
#
# Monthes_List
# @admin.register(main_menu)
# class main_menu_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
#         #
#         # Add aFilter Box
#         list_filter = (
#         'm_menu_id'      ,
#         'm_menu_name'    ,
#         )
#         #
#         #
#         # Show Fields a List
#         list_display = (
#         # 'AM_MonthNumber'       , 
#         'm_menu_id'      , 
#         'm_menu_name'      , 
#         'm_menu_link'      , 

#         )
#         #
#         # search list
#         search_fields = ['m_menu_name']
#         #
#         #