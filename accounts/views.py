# from winreg import REG_QWORD
from multiprocessing import context
import django
from django.shortcuts import render  , redirect#
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.contrib.auth import  get_user_model #
from django.contrib.auth.views import TemplateView #
from django.views import View #
from accounts.forms import SignUpForm  #
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
from accounts.models import PersonalsMODEL , FinancialStatementsMODEL , DatesReceivingMoneyPaymentsMODEL , SubscribersDesiresMODEL
UserModel = get_user_model()
import pywhatkit as pwt # Send messages To WhatsApp
import random
#
#
#
########## Profile Users:-############################################################
# Display The my_Profile_delete_done Page
class LogoutConfirmClass(TemplateView):
    template_name = 'registration/logout_confirm.html' # The Page HTML to Display
#
# Display Them About Page
class LogoutDoneClass(TemplateView):
    template_name = 'registration/logout_done.html' # The Page HTML to Display
#
# Register On The site And Create a Profile
class SignupCLASS(View):
    form_class = SignUpForm # Form for Entering New User Data
    template_name = 'registration/signup.html' # The Name Of a Template To Display For The View Use
    #
    # (1) Show User Registration Form
    def get(self, request, *args, **kwargs):
        form = self.form_class() # Save The Registration Form In a Variable
        return render(request, self.template_name, {'form': form})
    #
    # (2) Save Data and Send Email
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) # Save The Registration Data In The Variable If It Is (POST)
        if form.is_valid(): # Verify That The Form Is Valid For Saving Its Data
            user = form.save(commit=False) # Stop Saving Data
            user.is_active = False # Deactivate The Account To Be Confirmed By Email
            user.save() # Save Data
            current_site = get_current_site(request) # Get the Current (Web Site) By Comparing The Domain With The Host Name
            subject = 'Activate Your ( Family Associatior ) Account' # Email Address
            message = render_to_string('registration/activate_account_by_email.html', { # Email content
                'user': user,
                'domain': current_site.domain, # The Domain Name That Will Send The Message
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), # URL Safe Encode
                'token': default_token_generator.make_token(user),}) # Create a Special Code Sent To The e-Mail To Activate The Account
            user.email_user(subject, message) # Send E-mail(content - Address)
            messages.success(request, ('Please Confirm Your Email To Complete Registration.'))# Display Message For The New User(In His Email)
            # Display Message For The New User On The Registration Page
            return render(request, 'registration/confirm_email_registration.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
        else:
            # Reload The Form  Registration Agin
            return render(request, self.template_name, {'form': form})
#
# Activate E-mail
class ActivateCLASS(View):
    def get(self, request, uidb64  , token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True # User Activation
            user.save() # Data Save
            # Show Confirm Email Registration Form And Dysplay Message For Successful Operation
            return render(request, 'registration/confirm_email_registration_done.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
        else:
            # Show Activation Link Invalid Form For Unsuccessful Operation
            return render(request, 'registration/activation_link_invalid.html')
#
#

class DuesRecordListViewSearchCLASS(LoginRequiredMixin , ListView):
    paginate_by = 4  # if pagination is desired
    template_name = 'registration/dues_record_list.html'# The Page HTML to Display
    context_object_name = 'queryset_dues_record_list_CONTEXT'
#
    # def dues_record_list_views_search_DEF(self):
    def get_queryset(self):
        # Show All Records
        # data_from_multiple_tables = User.objects.all().select_related()\
        queryset_dues_record_list_CONTEXT = User.objects.all().select_related()\
                .values(
                # (1) User Model Fields 
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_active',
                'is_staff',
                'is_superuser',
                'last_login',
                'date_joined',
                # (2) Personal Model Fields - The Table Name Must Be Lower Case
                'personalsmodel__P_FirstName',
                'personalsmodel__P_FatherName',
                'personalsmodel__P_GrandFatherName',
                'personalsmodel__P_FamilyName',
                'personalsmodel__P_Mobile',
                'personalsmodel__P_Address',
                'personalsmodel__P_Notes',
                # (3) Financial Statements  Model Fields - The Table Name Must Be Lower Case
                'financialstatementsmodel__FS_User',
                'financialstatementsmodel__FS_SubscriptionAmount',
                'financialstatementsmodel__FS_NumberPaymentsDue',
                'financialstatementsmodel__FS_BankName',
                'financialstatementsmodel__FS_BankAccount',
                'financialstatementsmodel__FS_Notes',
                # (4) Dates Receiving Money Payments Model Fields -  The Table Name Must Be Lower Case
                'datesreceivingmoneypaymentsmodel__DRMP_User',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short',
                'datesreceivingmoneypaymentsmodel__DRMP_Notes',
                # Sort Fields By 'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long' Field
                ).order_by('datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long')
#
        # For Further Information: https://www.w3schools.com/django/django_ref_field_lookups.php
        # Save User Input To The Variable
        # Search By Number
        query = self.request.GET.get('search_by_number')
        if query:
            queryset_dues_record_list_CONTEXT = User.objects.filter( 
            Q(id=query)                                             |# ID Number
            Q(personalsmodel__P_Mobile=query)                       |# Mobile
            Q(financialstatementsmodel__FS_SubscriptionAmount=query)|# Subscription Amount
            Q(financialstatementsmodel__FS_NumberPaymentsDue=query)  # Number Payments Due
            ).select_related()\
                .values(
                # (1) User Model Fields 
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_active',
                'is_staff',
                'is_superuser',
                'last_login',
                'date_joined',
                # (2) Personal Model Fields - The Table Name Must Be Lower Case
                'personalsmodel__P_FirstName',
                'personalsmodel__P_FatherName',
                'personalsmodel__P_GrandFatherName',
                'personalsmodel__P_FamilyName',
                'personalsmodel__P_Mobile',
                'personalsmodel__P_Address',
                'personalsmodel__P_Notes',
                # (3) Financial Statements  Model Fields - The Table Name Must Be Lower Case
                'financialstatementsmodel__FS_User',
                'financialstatementsmodel__FS_SubscriptionAmount',
                'financialstatementsmodel__FS_NumberPaymentsDue',
                'financialstatementsmodel__FS_BankName',
                'financialstatementsmodel__FS_BankAccount',
                'financialstatementsmodel__FS_Notes',
                # (4) Dates Receiving Money Payments Model Fields -  The Table Name Must Be Lower Case
                'datesreceivingmoneypaymentsmodel__DRMP_User',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short',
                'datesreceivingmoneypaymentsmodel__DRMP_Notes',
                # Sort Fields By 'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long' Field
                ).order_by('datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short')
#
        # Save User Input To The Variable
        query = self.request.GET.get('search_by_letters')
        if query:
            queryset_dues_record_list_CONTEXT = User.objects.filter( 
            Q(first_name__icontains=query)                       |# First Name
            Q(last_name__icontains=query)                        |# Last Name
            Q(email__exact=query)                                |# Email
            Q(personalsmodel__P_FirstName__icontains=query)      |# First Name
            Q(personalsmodel__P_FatherName__icontains=query)     |# Father Name
            Q(personalsmodel__P_GrandFatherName__icontains=query)|# Grand Father Name
            Q(personalsmodel__P_FamilyName__icontains=query)      # Family Name
            ).select_related()\
                .values(
                # (1) User Model Fields 
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_active',
                'is_staff',
                'is_superuser',
                'last_login',
                'date_joined',
                # (2) Personal Model Fields - The Table Name Must Be Lower Case
                'personalsmodel__P_FirstName',
                'personalsmodel__P_FatherName',
                'personalsmodel__P_GrandFatherName',
                'personalsmodel__P_FamilyName',
                'personalsmodel__P_Mobile',
                'personalsmodel__P_Address',
                'personalsmodel__P_Notes',
                # (3) Financial Statements  Model Fields - The Table Name Must Be Lower Case
                'financialstatementsmodel__FS_User',
                'financialstatementsmodel__FS_SubscriptionAmount',
                'financialstatementsmodel__FS_NumberPaymentsDue',
                'financialstatementsmodel__FS_BankName',
                'financialstatementsmodel__FS_BankAccount',
                'financialstatementsmodel__FS_Notes',
                # (4) Dates Receiving Money Payments Model Fields -  The Table Name Must Be Lower Case
                'datesreceivingmoneypaymentsmodel__DRMP_User',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short',
                'datesreceivingmoneypaymentsmodel__DRMP_Notes',
                # Sort Fields By 'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long' Field
                ).order_by('datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short')
#
        # Save User Input To The Variable
        query = self.request.GET.get('search_by_dates')
        if query:
            queryset_dues_record_list_CONTEXT = User.objects.filter( 
            Q(datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long__icontains=query) |# Date Receiving Money Payments-Long
            Q(datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short__icontains=query) # Date Receiving Money Payments-Short
            ).select_related()\
                .values(
                # (1) User Model Fields 
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_active',
                'is_staff',
                'is_superuser',
                'last_login',
                'date_joined',
                # (2) Personal Model Fields - The Table Name Must Be Lower Case
                'personalsmodel__P_FirstName',
                'personalsmodel__P_FatherName',
                'personalsmodel__P_GrandFatherName',
                'personalsmodel__P_FamilyName',
                'personalsmodel__P_Mobile',
                'personalsmodel__P_Address',
                'personalsmodel__P_Notes',
                # (3) Financial Statements  Model Fields - The Table Name Must Be Lower Case
                'financialstatementsmodel__FS_User',
                'financialstatementsmodel__FS_SubscriptionAmount',
                'financialstatementsmodel__FS_NumberPaymentsDue',
                'financialstatementsmodel__FS_BankName',
                'financialstatementsmodel__FS_BankAccount',
                'financialstatementsmodel__FS_Notes',
                # (4) Dates Receiving Money Payments Model Fields -  The Table Name Must Be Lower Case
                'datesreceivingmoneypaymentsmodel__DRMP_User',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long',
                'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short',
                'datesreceivingmoneypaymentsmodel__DRMP_Notes',
                # Sort Fields By 'datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Long' Field
                ).order_by('datesreceivingmoneypaymentsmodel__DRMP_DateReceivingMoneyPayments_Short')

        # Send Page HTML & Context
        return  queryset_dues_record_list_CONTEXT

# Display List Record
class ProfileListViewSearchCLASS(LoginRequiredMixin , ListView):
    paginate_by = 4  # if pagination is desired
    template_name = 'registration/profile_list.html'# The Page HTML to Display
    context_object_name = 'queryset_users_list_CONTEXT'
    #
    def get_queryset(self):
        queryset_users_list_CONTEXT = User.objects.all()
        # queryset_personal_list = PersonalData_MODEL.objects.all()
        query = self.request.GET.get('q')# Save Searvh Criterian In a Variable
        if query:
            # Save Search Results In a Variable
            queryset_users_list_CONTEXT = User.objects.filter( 
                                            # Q(id__icontains=query)          |# ID Number
                                            Q(first_name__icontains=query)  |# First Name
                                            Q(last_name__icontains=query)   |# Last Name
                                            Q(email__icontains=query)        # Email
                                            # Q(is_active__icontains=query)    # User Is Active

        )
        return queryset_users_list_CONTEXT  # Send Search Results To The Disired  Page HTML
    ##
    #Send Extra Data To Pahge HTML
    def get_context_data(self, **kwargs):
        context_CONTEXT = super().get_context_data(**kwargs)
        context_CONTEXT['now'] =  timezone.now()
        return context_CONTEXT # Send This Data To The Required Page HTML

# Display Detail Record By: ID
class ProfileDetailIdCLASS(LoginRequiredMixin , DetailView):
    model = User # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/profile_detail_id.html'# The Page HTML to Display
#
# Update Profile.
class ProfileUpdateCLASS(UpdateView):
        model = User # Data Table
        template_name = 'registration/profile_update.html'# The Page HTML to Display
        success_url = reverse_lazy('ProfileUpdateDoneURL')# Go to This Page After Successful Operation
        fields = [ # Fields Table
            # 'username',
            # 'first_name',
            # 'last_name',
            'email',
            # 'last_login',
            # 'is_superuser',
            # 'is_staff',
            # 'is_active',
            # 'date_joined',
            ]
#
# Display The my_Profile_delete_done Page
class ProfileUpdateDoneCLASS(TemplateView):
    template_name = 'registration/profile_update_done.html' # The Page HTML to Display
#
# Delete Record.
class ProfileDeleteCLASS(LoginRequiredMixin  , DeleteView):
    model = User # Data Table
    template_name = 'registration/profile_confirm_delete.html' # The Page HTML to Display
    success_url = reverse_lazy('ProfileDeleteDoneURL') # Go to This Page After Successful Operation
#
# Display The my_Profile_delete_done Page
class ProfileDeleteDoneCLASS(TemplateView):
    template_name = 'registration/profile_delete_done.html' # The Page HTML to Display
#

# ########## Personal Data:-############################################################
## Display Detail Record By: ID
class PersonalDetailIdCLASS(LoginRequiredMixin , DetailView):
    model = PersonalsMODEL # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/personal_detail_id.html'# The Page HTML to Display
#
#
# # Update Profile.
class PersonalDataUpdateCLASS(UpdateView):
        model = PersonalsMODEL # Data Table
        template_name = 'registration/personal_update.html'# The Page HTML to Display
        success_url = reverse_lazy('PersonalDataUpdateDoneURL')# Go to This Page After Successful Operation
        fields = [ # Fields Table

            # 'P_User'                ,
            # 'slug'                  ,
            'P_FirstName'             ,
            'P_FatherName'            ,
            'P_GrandFatherName'       ,
            'P_FamilyName'            ,
            'P_Photo'                 ,
            'P_Mobile'                ,
            'P_Address'               ,
            'P_Notes'                 ,
            ]
#
# Display The my_Profile_delete_done Page
class PersonalDataUpdateDoneCLASS(TemplateView):
    template_name = 'registration/personal_data_update_done.html' # The Page HTML to Display
#
#
#
########## Financial Data:-####################################################################################################################################
## Display Detail Record By: ID
class FinancialStatementsDetailIdCLASS(LoginRequiredMixin , DetailView):
    model = FinancialStatementsMODEL # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/financial_statement_detail_id.html'# The Page HTML to Display
#
# Update Housing Record.
class FinancialStatementsUpdateCLASS(UpdateView):
        model = FinancialStatementsMODEL # Data Table
        template_name = 'registration/financial_statement_update.html'# The Page HTML to Display
        success_url = reverse_lazy('FinancialStatementsUpdateDoneURL')# Go to This Page After Successful Operation
        fields = [ # Fields Table
            ''
            # 'FS_User'               ,
            'FS_SubscriptionAmount' ,
            # 'FS_NumberPaymentsDue'  ,
            'FS_BankName'           ,
            'FS_BankAccount'        ,
            'FS_Notes'              ,
            ]
#
#
# Display The my_Housing_Data_done Page
class FinancialStatementsUpdateDoneCLASS(TemplateView):
    template_name = 'registration/financial_statement_update_done.html' # The Page HTML to Display
#
#
#
# ########## DATA RECEIVING MONEY PAYMENTS :-############################################################
## Display Detail Record By: ID
class DatesReceivingMoneyPaymentsDetailIdCLASS(LoginRequiredMixin , DetailView):
    model = DatesReceivingMoneyPaymentsMODEL # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/dates_receiving_money_payments_detail_id.html'# The Page HTML to Display
#
#
# Update Record  .
class DatesReceivingMoneyPamentsUpdateCLASS(UpdateView):
        model = DatesReceivingMoneyPaymentsMODEL # Data Table
        template_name = 'registration/dates_receiving_money_paments_update.html'# The Page HTML to Display
        success_url = reverse_lazy('DatesReceivingMoneyPamentsUpdateDoneURL')# Go to This Page After Successful Operation
        fields = [ # Fields Table
            # 'DRMP_User'                              ,
            'DRMP_DateReceivingMoneyPayments_Long'   ,
            'DRMP_DateReceivingMoneyPayments_Short'  ,
            'DRMP_Notes'                             ,
            ]
#
#
# Display Dates Receiving Money Paments Udate Done
class DatesReceivingMoneyPamentsUpdateDoneCLASS(TemplateView):
    template_name = 'registration/dates_receiving_money_paments_update_done.html' # The Page HTML to Display
#
#
#
# Display Detail Record By: ID
class SubscribersDesiresDetailIdCLASS(LoginRequiredMixin , DetailView):
    model = SubscribersDesiresMODEL # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/subscribers_desires_detail_id.html'# The Page HTML to Display
#
#
#
# # Update Profile.
class SubscribersDesiresUdateCLASS(UpdateView):
        model = SubscribersDesiresMODEL # Data Table
        template_name = 'registration/subscribers_desires_update.html'# The Page HTML to Display
        success_url = reverse_lazy('SubscribersDesiresUdateDoneURL')# Go to This Page After Successful Operation
        fields = [ # Fields Table

            # 'SD_User'            ,
            'SD_Desire_first'      ,
            'SD_Desire_second'     ,
            'SD_Desire_third'      ,
            'SD_Notes'             ,
            ]
#
#
#
# Display Dates Receiving Money Paments Udate Done
class SubscribersDesiresUdateDoneCLASS(TemplateView):
    template_name = 'registration/subscribers_desires_update_done.html' # The Page HTML to Display
#
#
# class My_Profile_Delete_Multiple_Select(LoginRequiredMixin, ListView):
#     context_object_name = 'entry_list' # Data List To Send Page HTML
#     paginate_by =  5
#     model = User # Table Name In Database
#     template_name = "portfolios/entry_list.html" # Page HTML Containing The Data List

#     def get_queryset(self):
#         return User.objects.filter(created_by=self.request.user).order_by('-pk')

#     def post(self, request, *args, **kwargs):
#         ids = self.request.POST.get('ids', "")
#         # ids if string like "1,2,3,4"
#         ids = ids.split(",")
#         try:
#             # Check ids are valid numbers
#             ids = map(int, ids)
#         except ValueError as e:
#             return JsonResponse(status=400)
#         # delete items
#         self.model.objects.filter(id__in=ids).delete()
#         return JsonResponse({"status": "ok"}, status=204)
#
#
# # class My_Profile_ListView_Search(LoginRequiredMixin , TemplateView):
# # #     paginate_by = 4  # if pagination is desired
# #     template_name = 'registration/my_profile_list.html'# The Page HTML to Display
# #     context_object_name = 'queryset_users_list'
# #     #

# #     def get_context_data(self, **kwargs):
# #         query = self.request.GET.get('q')# Save Searvh Criterian In a Variable
# #         if query:
# #             context = super().get_context_data(**kwargs)
# #             context['queryset_users_list'] = User.objects.filter(id__icontains=query)
# #             context['queryset_personal_data'] = PersonalData_MODEL.objects.filter(id__icontains=query)
# #             return context
# #         else:
# #             context = super().get_context_data(**kwargs)
# #             context['queryset_users_list'] = User.objects.all()
# #             context['queryset_personal_data'] = PersonalData_MODEL.objects.all()
# #             return context

#     # def get_queryset(self):
#     #     object_list = User.objects.all()
#     #     # object_list_personal = PersonalData_MODEL.objects.all()
#     #     query = self.request.GET.get('q')# Save Searvh Criterian In a Variable
#     #     if query:
#     #         # Save Search Results In a Variable
#     #         object_list = User.objects.filter(
#     #         Q(id__icontains=query)             # ID Number
#     #         # Q(id__icontains=query)          |# ID Number
#     #         # Q(first_name__icontains=query)  |# First Name
#     #         # Q(last_name__icontains=query)   |# Last Name
#     #         # Q(email__icontains=query)       | # Email
#     #         # Q(is_active__icontains=query)    # User Is Active

#     #     )
#     #     return object_list  # Send Search Results To The Disired  Page HTML
#         #
# # # Django - multiple models(table) in one view - Stack Overflow
# # class My_Profile_ListView_Search_01(LoginRequiredMixin , ListView):
# #     context_object_name = 'home_list'
# #     template_name = 'contacts/index.html'
# #     queryset = Individual.objects.all()

# #     def get_context_data(self, **kwargs):
# #         context = super(IndexView, self).get_context_data(**kwargs)
# #         context['roles'] = Role.objects.all()
# #         context['venue_list'] = Venue.objects.all()
# #         context['festival_list'] = Festival.objects.all()
# #         # And so on for more models
# #         return context
#
# # Display Detail Record By: Slug
# class My_Profile_Detail_Slug(LoginRequiredMixin ,  DetailView):
#     model = User # Data Table
#     slug_field = 'ASS_Slug' # Filter Field Use 'Slug'
#     context_object_name = 'My_Object' # Data To Be Sent To Page HTML
#     template_name = 'registration/my_profile_detail_slug.html'# The Page HTML to Display
#































# from twilio.rest import Client
# account_sid=''
# auth_token =''
# client = Client(account_sid , auth_token)
# def send_sms(user_code , phone_number):
#     messages = client.messages.create(body =f'Hie ! Your user and verification code is {user_code}',from_ ='',to=f'{phone_number}')  
# print(messages.sid)                       
# class My_Dues_Record_ListView_Search(LoginRequiredMixin , TemplateView):
# #     paginate_by = 4  # if pagination is desired
#     template_name = 'registration/my_dues_record_list.html'# The Page HTML to Display
#     # context_object_name = 'queryset_dues_record_list'
#     #

#     def get_context_data(self, **kwargs):
#         query = self.request.GET.get('search_tool')# Save Searvh Criterian In a Variable
#         # verify that The Searvh Tool Is Not Empty Of Data
#         if query:
#             context = super().get_context_data(**kwargs)
#             # Fill in the list from the database
#             context['queryset_monthes_menu'] = Monthes_Menu_MODEL.objects.all()
#             # Display Data After Filtering
#             context['queryset_dues_record_list']    = Association_Months_MODEL.objects.filter(AM_MonthName__icontains=query)

#             return context
#         else:
#             context = super().get_context_data(**kwargs)
#             # Fill in the list from the database
#             context['queryset_monthes_menu'] = Monthes_Menu_MODEL.objects.all()
#             #Display All Data
#             context['queryset_dues_record_list']    = Association_Months_MODEL.objects.all()
#             return context
# #
# #
# # # Search Withe Dynamic Menu
# class My_Monthes_Menu(LoginRequiredMixin , ListView):
#     # paginate_by = 4  # if pagination is desired
#     template_name = 'registration/my_dues_record_list.html'# The Page HTML to Display
#     context_object_name = 'queryset_monthes_menu'
#     #
#     def get_queryset(self):
#         queryset_monthes_menu = Monthes_Menu_MODEL.objects.all()
#         # queryset_personal_list = PersonalData_MODEL.objects.all()
#         return queryset_monthes_menu  # Send Search Results To The Disired  Page HTML





# from django.shortcuts import render, redirect
# from django.contrib import auth
# from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from accounts.models import main_menu, sub_menu


# # Create your views here.

# def countown(request):
#     return render(request, 'count.html')


# def maninmenu(request):
#     menu = main_menu.objects.all()
#     submenu=sub_menu.objects.all()
#     return render(request, 'menu.html', {'menu': menu,'submenu':submenu})


# def mainsave(request):
#     if request.method == 'POST':
#         mname = request.POST['menu_name']
#         mlink = request.POST['mn_link']
#         main_menu.objects.create(m_menu_name=mname, m_menu_link=mlink)
#         # return HttpResponse("created")
#         return redirect('mainmenu')
#     else:
#         return redirect('mainmenu')


# def subsave(request):
#     if request.method == 'POST':
#         menuid=request.POST['parent']
#         sname=request.POST['sub_menu_name']
#         slink=request.POST['sub_menu_link']
#         sub_menu.objects.create(m_menu_id=menuid,s_menu_name=sname,s_menu_link=slink)
#         return redirect('mainmenu')
#     else:
#         return redirect('mainmenu')

# def dynamic_menu(request):
#     menu = main_menu.objects.all()
#     submenu = sub_menu.objects.all()
#     return render(request, 'dynamic_menu.html', {'menu': menu, 'submenu': submenu})

# Select Data from Multiple Tables In One Query 

# ==================================================================================================================
# def save(self):
#     new_user  = User.objects.create_user(first=self.cleaned_data['first'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
#     new_grade = PersonalsMODEL.objects.create_P_Mobile(grade=self.cleaned_data['P_Mobile'])
#     return new_user, new_grade 


# def save(self, commit=True):
#     if not commit:
#         raise NotImplementedError("Can't create User and UserProfile without database save")
#     user         = super(UserCreateForm, self).save(commit=True)
#     user_profile = PersonalsMODEL(user=user, P_Mobile=self.cleaned_data['Mobile'])
#     user_profile.save()
#     return user, user_profile
# ==================================================================================================================
# from .forms import SignUpForm , ProfileForm

# #newly added function
# # def update_user_data(user):
# #     Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob},)
# def update_user_data(user):
#     PersonalsMODEL.objects.update_or_create(user=user, defaults={PersonalsMODEL.P_Mobile},)


# class SignupCLASS___(View):
#     form_class = SignUpForm # Form for Entering New User Data
#     template_name = 'registration/signup.html' # The Name Of a Template To Display For The View Use
#     #
#     # (1) Show User Registration Form
#     def get(self, request, *args, **kwargs):
#         form = self.form_class() # Save The Registration Form In a Variable
#         return render(request, self.template_name, {'form': form})
#     #
#     # (2) Save Data and Send Email
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST) # Save The Registration Data In The Variable If It Is (POST)
#         if form.is_valid(): # Verify That The Form Is Valid For Saving Its Data
#             user = form.save(commit=False) # Stop Saving Data
#             user.is_active = False # Deactivate The Account To Be Confirmed By Email
#             user.save() # Save Data
#             # profile_data=PersonalsMODEL(P_Mobile='9660000000000', P_User=user)
#             # profile_data.save()
            
            
#             # PersonalsMODEL.objects.create(P_User=user ,P_Mobile='9660000000000')
#             pro=PersonalsMODEL(P_User=user ,P_Mobile='9660000000000')
#             pro.save()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             current_site = get_current_site(request) # Get the Current (Web Site) By Comparing The Domain With The Host Name
#             subject = 'Activate Your ( Family Associatior ) Account' # Email Address
#             message = render_to_string('registration/activate_account_by_email.html', { # Email content
#                 'user': user,
#                 'domain': current_site.domain, # The Domain Name That Will Send The Message
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)), # URL Safe Encode
#                 'token': default_token_generator.make_token(user),}) # Create a Special Code Sent To The e-Mail To Activate The Account
#             user.email_user(subject, message) # Send E-mail(content - Address)
#             messages.success(request, ('Please Confirm Your Email To Complete Registration.'))# Display Message For The New User(In His Email)
#             # Display Message For The New User On The Registration Page
#             return render(request, 'registration/confirm_email_registration.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
#         else:
#             # Reload The Form  Registration Agin
#             return render(request, self.template_name, {'form': form})



# def SignupDEF_____(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.P_Mobile='+966506361923'
#             profile.save()
#             context = {'form':form , 'profile_form':profile_form}
#             return render(request , 'registration/signup.html' ,context)
#     else:
#         form         = SignUpForm()
#         profile_form = ProfileForm()
#     context = {'form':form , 'profile_form':profile_form}
#     return render(request , 'registration/signup.html' ,context)
# #

# from .models import Profile
# from .forms import SignUpForm
# from django.db.models.signals import post_save , post_delete # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده

# #newly added function
# def update_user_data(user):
#     Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob},)

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             ####
#             def create_Profile(sender, **kwargs):
#                 if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
#                     Profile.objects.create(user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
#             # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
#             post_save.connect(create_Profile , sender=User)

#             ######
#             user = form.save()
#             user.profile.mob = form.cleaned_data.get('mob')
#             update_user_data(user)  

#             user.refresh_from_db()

#             #newly added
#             # user.profile.mob = form.cleaned_data.get('mob')
#             # update_user_data(user)  

#             # load the profile instance created by the signal

#             user.save()
#             # raw_password = form.cleaned_data.get('password1')

#             # login user after signing up
#             # user = authenticate(username=user.username, password=raw_password)
#             # login(request, user)

#             # redirect user to home page
#             return redirect('index_pageURL')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})