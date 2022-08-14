from django.contrib import admin
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from accounts.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
# 
# Aplications OTP
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
#
"""Important Note:
(fields) & (fieldsets) This Properties Can Not Be Put Together
# Controlling Which fields are Displayed and Laid Out
# fields = [('ASS_NameAssociation', 'ASS_Slug' ), 'ASS_AssociationLogo' , 'ASS_Address' ,('ASS_Mobile' , 'ASS_Phone') , 'ASS_Email' , 'ASS_BankAccount']
"""
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
#========== Django Admin – Redesign and Customization ==Start=========================
#
# (1) Changing the Django administration header and Titel text
# Modifying The Site Admin Page
# admin.site.site_header = "Family Associatior"    # Site Header
# admin.site.site_title = "Family Associatior"     # Site Tab Title
# admin.site.index_title = "Administration Portal" # Site Index Page Title
#
# (2) Removing the any group
# from  django.contrib.auth.models  import  Group #  import it then unregister it in admin.py.
# admin.site.unregister(User) # unregister the existing users
# admin.site.unregister(Group) # unregister Group From Admin Site
#
# (3) Using OTP
# # Adding The Ability to Access The Admin page Using OTP
# admin.site.__class__ = OTPAdminSite 
#
# (4)change django admin "view site" link to custom absolute url
# admin.site.site_url = "/mySite"
#==========Customize the Django Admin Site==End========================================
#
# Personal File
@admin.register(PersonalsMODEL)
class PersonalsADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add a Search Box With The Fields Below:
        search_fields = ('P_User','P_FirstName', 'P_FatherName', 'P_GrandFatherName','P_FamilyName','P_Mobile' , 'image_tag', 'full_name')
        #
        #
        # Automatically Fill In Slug Field From Variable (FullName)
        # FullName = {
        # "slug": # Slug Field
        # [
        # 'P_FirstName'       , 
        # 'P_FatherName'      ,
        # 'P_GrandFatherName' ,
        # 'P_FamilyName'
        # ]
        # } # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
        # prepopulated_fields = FullName
        #
        # 
        # Add a Filter Box
        list_filter = (
        'P_User'     , 
        'P_Mobile'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'P_User'                  , 
        'slug'                    ,
        'full_name'               ,
        'image_tag'               ,
        'P_FirstName'             ,
        'P_FatherName'            ,
        'P_GrandFatherName'       ,
        'P_FamilyName'            ,
        'P_Photo'                 ,
        'P_Mobile'                ,
        'P_Address'               ,
        'P_Notes'
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, 
        {
        'fields': (
        'P_User'              ,
        'slug'              ,
        'P_FirstName'         ,
        'P_FatherName'        ,
        'P_GrandFatherName'   ,
        'P_FamilyName'        ,
        'P_Mobile'                ,
        'P_Address'           
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',),
        'fields': (
        'P_Photo'            ,
        'P_Notes'    
        )
        }
        ),
        )
# 
# Financial Statements
@admin.register(FinancialStatementsMODEL)
class FinancialStatementsADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add a Search Box With The Fields Below:
        search_fields = ('FS_User','FS_BankAccount', 'FS_SubscriptionAmount', 'FS_NumberPaymentsDue')
        #
        # Add a Search Box With The Fields Below:
        search_fields = ('first_name', 'last_name', 'email')
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
        'FS_SubscriptionAmount'        , 
        'FS_NumberPaymentsDue'         , 
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
@admin.register(DatesReceivingMoneyPaymentsMODEL)
class DatesReceivingMoneyPaymentsADMIN(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add a Search Box With The Fields Below:
        search_fields = ('DRMP_User', 'DRMP_DateReceivingMoneyPayments_Long', 'DRMP_DateReceivingMoneyPayments_Short')
        #
        # Add aFilter Box
        list_filter = (
        'DRMP_User'      , 
        'DRMP_DateReceivingMoneyPayments_Long'   ,
        'DRMP_DateReceivingMoneyPayments_Short'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'DRMP_User'     , 
        'DRMP_DateReceivingMoneyPayments_Long'   , 
        'DRMP_DateReceivingMoneyPayments_Short'  , 
        'DRMP_Notes'
        )
        #
        # search list
        search_fields = ['DRMP_DateReceivingMoneyPayments_Long']

        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'DRMP_User'                        , 
        'DRMP_DateReceivingMoneyPayments_Long'   , 
        'DRMP_DateReceivingMoneyPayments_Short'  
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',) ,
        'fields': (
        'DRMP_Notes',
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
#
#
#
# Dates Receiving Payments
@admin.register(SubscribersDesiresMODEL)
class SubscribersDesiresMODELADMIN(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add a Search Box With The Fields Below:
        search_fields = ('SD_User', 'SD_Desire', 'SD_Notes')
        editable_list = ['SD_User', 'SD_Desire', 'SD_Notes'] 

        #
        # Add aFilter Box
        list_filter = (
        'SD_User'      , 
        'SD_Desire_first'   ,
        'SD_Desire_second'  ,
        'SD_Desire_third'   ,
        'SD_Notes'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'SD_User'     , 
        'SD_Desire_first'   ,
        'SD_Desire_second'  ,
        'SD_Desire_third'   ,
        'SD_Notes'
        )
        #
        # search list
        search_fields = ['SD_Desire']

        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'SD_User'         , 
        'SD_Desire_first'   ,
        'SD_Desire_second'  ,
        'SD_Desire_third'
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',) ,
        'fields': (
        'SD_Notes',
        )
        }
        ),
        )



# 
# """Admin OTP
# class OTPAdmin(OTPAdminSite):
#         pass
# #
# admin.site= OTPAdmin(name="OTPAdmin")
# admin.site.register(User)
# admin.site.register(PersonalsMODEL)
# admin.site.register(FinancialStatementsMODEL)
# admin.site.register(DatesReceivingMoneyPaymentsMODEL)
# admin.site.register(TOTPDevice)
# """

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib import admin
# from django.contrib.auth.models import Group, User

# # first unregister the existing useradmin...
# admin.site.unregister(User)

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
#     fieldsets = (
#     (None, {'fields': ('username', 'password')}),
#     ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
#     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#     ('Important dates', {'fields': ('last_login', 'date_joined')}),)
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')}),)
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('username', 'first_name', 'last_name', 'email')
#     ordering = ('username',)
#     filter_horizontal = ('groups', 'user_permissions',)

# # Now register the new UserAdmin...
# admin.site.register(User, UserAdmin)
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


# @admin.register(Profile)
# class ProfileADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
#         #
#         # Add a Search Box With The Fields Below:
#         search_fields = ('P_User','P_FirstName', 'P_FatherName', 'P_GrandFatherName','P_FamilyName','P_Mobile')
#         #
#         #
#         # Add a Filter Box
#         list_filter = (
#         'user'     , 
#         'mobile'
#         )
#         #
#         #
#         # Show Fields a List
#         list_display = (
#         'user'  ,
#         'mobile'
#         )

