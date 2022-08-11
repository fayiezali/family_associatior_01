from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views # This Views Built-in Django
from accounts import views # This Views I Created It
#
# AUTHENTICATION:-------------------------------------------------------------------------------------------------------
# Login - Logout - Logout Confirm - Logout Done (1) Login (1)
urlpatterns = [
        # Login In System
        # This Was Created By django
        path('login/'                                   , auth_views.LoginView.as_view()         , name='login'),
        # Exit From System
        # thies Was Created By Django
        path('logout/'                                  , auth_views.LogoutView.as_view()        , name='logout'),
        # Logout Confirme
        # This is me created by me
        path('logout_confirm/'                          , views.LogoutConfirmClass.as_view()     , name='LogoutConfirmURL'),
        # Checkout Confirmed Successfull
        path('logout_done/'                             , views.LogoutDoneClass.as_view()        , name='LogoutDoneURL'),
]
# Change Password - Password Change Done (2)
urlpatterns += [
        # thies Was Created By Django
        # Change Password
        path('change-password/'                         , auth_views.PasswordChangeView.as_view(
        template_name='registration/change-password.html', # The Name Of a Template To Display For The View Use
        success_url= reverse_lazy('password_change_done')), # Redirect To URL Address
        name='password_change'), # Name URL pattern
        #
        # Password Change completed Succesfull
        # thies Was Created By Django
        path('password_change_done/'                   , auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password-change-done.html'), # The Name Of a Template To Display For The View Use
        name='password_change_done'), # Name URL pattern
# Password Reset - Password Reset Done - Password Reset Confirm - Password Reset Comlete (3)
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
        # The URL To Redirect To After a Successful Password Reset Request
        # thies Was Created By Django
        path('password-reset/'                         , auth_views.PasswordResetView.as_view(
        template_name='registration/password_resetHTML.html', # The Name Of a Template To Display For The View Use
        subject_template_name='registration/password_reset_subject.txt',
        success_url= reverse_lazy('password_reset_done')), # Redirect To URL Address
        name='password_reset'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset/done/'                    , auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_doneHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_done'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirmHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_confirm'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset-complete/'               , auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_completeHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_complete'), # Name URL pattern
]
# PROFILE DATA:-------------------------------------------------------------------------------------------------------
urlpatterns += [
        # Signup And Confirm Registration With Email
        path('signup/'                            , views.SignupCLASS.as_view()                       , name='SignupURL'),
        # Active Registration Withe Email.
        path('activate/<uidb64>/<token>/'         , views.ActivateCLASS.as_view()                     , name='ActivateURL'),
        # View  Record Details  By (ID)
        path('profile_detail_id/<int:pk>/'        , views.ProfileDetailIdCLASS.as_view()              , name='ProfileDetailIdURL'),
        # Update Record
        path('profile_update/<int:pk>/'           , views.ProfileUpdateCLASS.as_view()                , name='ProfileUpdateURL'),
        # Checkout Confirmed Successfull
        path('profile_update_done/'               , views.ProfileUpdateDoneCLASS.as_view()            , name='ProfileUpdateDoneURL'),
        # Delete Record
        path('profile_delete/<int:pk>/delete/'    , views.ProfileDeleteCLASS.as_view()                , name='ProfileDeleteURL'),
        # Checkout Confirmed Successfull
        path('profile_delete_done/'               , views.ProfileDeleteDoneCLASS.as_view()            , name='ProfileDeleteDoneURL'),
        # View and Search The Records
        path('profile_list/'                      , views.ProfileListViewSearchCLASS.as_view()        , name='ProfileListViewSearchURL'),
        # View a List Of The Records
#*****************************************************************************************************
#       ## View Record Details By (slug)
#       # path('my_profile_detail_sluIDg/<slug:slug>/' , views.My_Profile_Detail_Slug.as_view()       , name='My_Profile_Detail_Slug_URL'),
#       # Delete Multiple Records Select
#       # path('Profile_delete/<int:pk>/delete/'    , views.My_Profile_Delete_Multiple_Select.as_view() , name='My_Profile_Delete_Multiple_Select_URL'),
#*****************************************************************************************************
#       #*********************************************************************************************
#       # Show Details In The Profile - But The code Is Written In The Model
#       # path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
#       # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
#       #*********************************************************************************************
]
# # PERSONAL DATA:-------------------------------------------------------------------------------------------------------
urlpatterns += [
        # View  Record Details  By (ID)
        path('personal_detail_id/<int:pk>/'         , views.PersonalDetailIdCLASS.as_view()           , name='PersonalDetailIdURL'),
        # Update Record
        path('personal_update/<int:pk>/'            , views.PersonalDataUpdateCLASS.as_view()         , name='PersonalDataUpdateURL'),
        # # Checkout Confirmed Successfull
        path('personal_data_update_done/'           , views.PersonalDataUpdateDoneCLASS.as_view()     , name='PersonalDataUpdateDoneURL'),
        # # Checkout Confirmed Successfull
        # path('my_personal_delete_done/'           , views.My_Profile_Delete_Done.as_view()          , name='My_Profile_Delete_Done_URL'),
]
# FINANCIAL STATEMENTS DATA:-------------------------------------------------------------------------------------------------------
urlpatterns += [
        # View  Record Details  By (ID)
        path('financial_statements_Detail_ID/<int:pk>/' , views.FinancialStatementsDetailIdCLASS.as_view()     , name='FinancialStatementsDetailIdURL'),
        # Update Record
        path('financial_statements_update/<int:pk>/'    , views.FinancialStatementsUpdateCLASS.as_view()       , name='FinancialStatementsUpdateURL'),
        # Checkout Confirmed Successfull
        path('financial_statements_update_done/'        , views.FinancialStatementsUpdateDoneCLASS.as_view()   , name='FinancialStatementsUpdateDoneURL'),
]
# DATES RECEIVING MONEY PAYMENTS DATA:-------------------------------------------------------------------------------------------------------
urlpatterns += [
        # View Record Details By (ID)
        path('dates_receiving_money_payments_detail_id/<int:pk>/'  , views.DatesReceivingMoneyPaymentsDetailIdCLASS.as_view()      , name='DatesReceivingMoneyPaymetsDetailIdURL'),
        # Update Record
        path('dates_receiving_money_payments_update/<int:pk>/'     , views.DatesReceivingMoneyPamentsUpdateCLASS.as_view()         , name='DatesReceivingMoneyPamentsUpdateURL'),
        # Checkout Confirmed Successfull
        path('dates_receiving_money_payments_update_done/'         , views.DatesReceivingMoneyPamentsUpdateDoneCLASS.as_view()     , name='DatesReceivingMoneyPamentsUpdateDoneURL'),
]
#
#
# # DUES RECORD:----------------------------------------------------------------------------------------
urlpatterns +=[
        # View and Search The Records List
        path('dues_record_list/'  ,views.DuesRecordListViewSearchCLASS.as_view()   , name='dues_record_list_views_searchURL'),
        #
        # path('save/'  ,views.save()   , name='saveURL'),
        #*********************************************************************************
]
# SUBSCRIBERS DESIRES DATA:-------------------------------------------------------------------------------------------------------
urlpatterns += [
        # View Record Details By (ID)
        path('subscribers_desires_detail_id/<int:pk>/'         , views.SubscribersDesiresDetailIdCLASS.as_view()      , name='SubscribersDesiresDetailIdURL'),
        # Update Record
        path('subscribers_desires_update/<int:pk>/'            , views.SubscribersDesiresUdateCLASS.as_view()         , name='SubscribersDesiresUdateURL'),
        # Checkout Confirmed Successfull
        path('subscribers_desires_update_done/'                , views.SubscribersDesiresUdateDoneCLASS.as_view()     , name='SubscribersDesiresUdateDoneURL'),
]


# urlpatterns += [
#     path('', views.countown, name='countdown'),
#     path('main',views.maninmenu,name='mainmenu'),
#     path('mainsave',views.mainsave,name='msave'),
#     path('submenusave',views.subsave,name='submenusave'),
#     path('dmenu',views.dynamic_menu,name='dmenu')
# ]

