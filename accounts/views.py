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
from accounts.models import ProfilesMODEL , FinancialStatementsMODEL , DatesReceivingMoneyPaymentsMODEL  
UserModel = get_user_model()
#
#
########## Profile Users:-############################################################
# Display The my_Profile_delete_done Page
class LogoutConfirmClass(TemplateView):
    template_name = 'registration/logout_confirm.html' # The Page HTML to Display
#
#
#
# Display Them About Page
class LogoutDoneClass(TemplateView):
    template_name = 'registration/logout_done.html' # The Page HTML to Display
#
#
#
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
#
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
#
#
#
#
# # Display List Record
# class My_Profile_ListView_Search(LoginRequiredMixin , ListView):    
#     paginate_by = 4  # if pagination is desired
#     template_name = 'registration/my_profile_list.html'# The Page HTML to Display
#     context_object_name = 'queryset_users_list'
#     #
#     def get_queryset(self):
#         queryset_users_list = User.objects.all()
#         # queryset_personal_list = PersonalData_MODEL.objects.all()
#         query = self.request.GET.get('q')# Save Searvh Criterian In a Variable
#         if query:
#             # Save Search Results In a Variable
#             queryset_users_list = User.objects.filter(
#             Q(id__icontains=query)             # ID Number
#             # Q(id__icontains=query)          |# ID Number
#             # Q(first_name__icontains=query)  |# First Name
#             # Q(last_name__icontains=query)   |# Last Name
#             # Q(email__icontains=query)       | # Email
#             # Q(is_active__icontains=query)    # User Is Active
            
#         )
#         return queryset_users_list  # Send Search Results To The Disired  Page HTML
#     ##
#     #Send Extra Data To Pahge HTML
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] =  timezone.now()
#         return context # Send This Data To The Required Page HTML

#     #
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


# #
# #
# #
# #
# #
# #
# # Display Detail Record By: Slug
# class My_Profile_Detail_Slug(LoginRequiredMixin ,  DetailView):
#     model = User # Data Table
#     slug_field = 'ASS_Slug' # Filter Field Use 'Slug'
#     context_object_name = 'My_Object' # Data To Be Sent To Page HTML
#     template_name = 'registration/my_profile_detail_slug.html'# The Page HTML to Display
# #
# #
# #
# ## Display Detail Record By: ID
# class My_Profile_Detail_ID(LoginRequiredMixin , DetailView):
#     model = User # Data Table
#     slug_field = 'pk' # Filter Field Use 'PK"
#     context_object_name = 'My_Object' # Data To Be Sent To Page HTML
#     template_name = 'registration/my_profile_detail_ID.html'# The Page HTML to Display
# #
# #
# #
# # Update Profile.
# class My_Profile_Update(UpdateView):
#         model = User # Data Table
#         template_name = 'registration/My_Profile_Update.html'# The Page HTML to Display
#         success_url = reverse_lazy('My_Profile_Update_Done_URL')# Go to This Page After Successful Operation
#         fields = [ # Fields Table
#             'username', 
#             'first_name',
#             'last_name',
#             'email',
#             # 'last_login',
#             # 'is_superuser', 
#             # 'is_staff', 
#             # 'is_active', 
#             # 'date_joined',
#             ]
# #
# #
# #
# # Display The my_Profile_delete_done Page
# class My_Profile_Update_Done(TemplateView):
#     template_name = 'registration/my_profile_update_done.html' # The Page HTML to Display

# # Delete Record.
# class My_Profile_Delete(LoginRequiredMixin  , DeleteView):
#     model = User # Data Table
#     template_name = 'registration/my_profile_confirm_delete.html' # The Page HTML to Display
#     success_url = reverse_lazy('My_Profile_Delete_Done_URL') # Go to This Page After Successful Operation
# #
# #
# #
# # Display The my_Profile_delete_done Page
# class My_Profile_Delete_Done(TemplateView):
#     template_name = 'registration/my_profile_delete_done.html' # The Page HTML to Display
# #
# #
# #
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
# #
# #
# #
# #
# #
# #
# ########## Personal Data:-############################################################
# ## Display Detail Record By: ID
# class My_Personal_Data_Detail_ID(LoginRequiredMixin , DetailView):
#     model = PersonalData_MODEL # Data Table
#     slug_field = 'pk' # Filter Field Use 'PK"
#     context_object_name = 'My_Object' # Data To Be Sent To Page HTML
#     template_name = 'registration/my_personal_data_detail_ID.html'# The Page HTML to Display
# #
# #
# # Update Profile.
# class My_Personal_Data_Update(UpdateView):
#         model = PersonalData_MODEL # Data Table
#         template_name = 'registration/my_personal_Update.html'# The Page HTML to Display
#         success_url = reverse_lazy('My_Personal_Data_Update_Done_URL')# Go to This Page After Successful Operation
#         fields = [ # Fields Table
            
#             'PER_User'              ,
#             'PER_Avialable'             , 
#             'FER_Slug'                  ,  
#             'PER_FirstName'             ,
#             'PER_GrandFatherName'       ,
#             'PER_FamilyName'             , 
#             'PER_ImgePersonal'          , 
#             'PER_IdNumber'              ,
#             'PER_Nationality'           ,
#             'PER_Mobile'                ,
#             ]
# #
# #
# # Display The my_Profile_delete_done Page
# class My_Personal_Data_Update_Done(TemplateView):
#     template_name = 'registration/my_personal_data_update_done.html' # The Page HTML to Display
# #
# #
# #
# #
# #
# #
# ########## Financial Data:-############################################################
# ## Display Detail Record By: ID
# class My_Financial_Data_Detail_ID(LoginRequiredMixin , DetailView):
#     model = FinancialData_MODEL # Data Table
#     slug_field = 'pk' # Filter Field Use 'PK"
#     context_object_name = 'My_Object' # Data To Be Sent To Page HTML
#     template_name = 'registration/my_financial_data_detail_ID.html'# The Page HTML to Display
# #
# #
# # Update Housing Record.
# class My_Financial_Data_Update(UpdateView):
#         model = FinancialData_MODEL # Data Table
#         template_name = 'registration/my_financial_data_Update.html'# The Page HTML to Display
#         success_url = reverse_lazy('My_Financial_Data_Update_Done_URL')# Go to This Page After Successful Operation
#         fields = [ # Fields Table
#             ''             
#             'FIN_ShareValue'             ,
#             'FIN_NumberShares'           ,       
#             'FIN_BankName'               ,                            
#             'FIN_BankAccount'            ,                                
#             'FIN_MethodPayment'          ,      
#             'FIN_MethodReceive'          ,
#             'FIN_SalaryDisbursementDate' ,                                              
#             'FIN_DateShareReceived'      ,                  
#             ]
# #
# #
# # Display The my_Housing_Data_done Page
# class My_Financial_Data_Update_Done(TemplateView):
#     template_name = 'registration/my_financial_data_update_done.html' # The Page HTML to Display
# #
# #
# #
# ########## Housing Data:-############################################################
# ## Display Detail Record By: ID
# class My_Housing_Data_Detail_ID(LoginRequiredMixin , DetailView):
#     model = HousingData_MODEL # Data Table
#     slug_field = 'pk' # Filter Field Use 'PK"
#     context_object_name = 'My_Object' # Data To Be Sent To Page HTML
#     template_name = 'registration/my_housing_data_detail_ID.html'# The Page HTML to Display
# #
# #
# # Update Housing Record.
# class My_Housing_Data_Update(UpdateView):
#         model = HousingData_MODEL # Data Table
#         template_name = 'registration/my_housing_data_Update.html'# The Page HTML to Display
#         success_url = reverse_lazy('My_Housing_Data_Update_Done_URL')# Go to This Page After Successful Operation
#         fields = [ # Fields Table
#             'HOU_User',
#             'HOU_Region', 
#             'HOU_City', 
#             'HOU_District',
#             'HOU_HomeAddress',
#             'HOU_CurrentWork', 
#             'HOU_WorkAddress', 
#             ]
# #
# #
# # Display The my_Housing_Data_done Page
# class My_Housing_Data_Update_Done(TemplateView):
#     template_name = 'registration/my_housning_data_update_done.html' # The Page HTML to Display
# #
# #
# #
# #
# #
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