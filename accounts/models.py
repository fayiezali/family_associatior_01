from signal import signal
# from blinker import receiver_connected
from django.db import models
#
from typing import ClassVar
#
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
from django.urls import reverse  # To generate URLS by reversing URL patterns
#
from django.dispatch import receiver
#
from django.db.models.signals import post_save , post_delete # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده
#
from django.utils.text import slugify
#
from datetime import datetime
#
from datetime import date
#
from twilio.rest import Client
#
from phonenumber_field.modelfields import PhoneNumberField
#
from django.core.mail import send_mail
# from django.core.mail import send_mail
from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS
# Send Whatsapp
import time
import webbrowser 
import pyautogui 
# Send OTP
import random
#
from django.utils.safestring import mark_safe
# from django.utils.translation import ugettext_lazy as _
####################################
# (1)Personal Data
class PersonalsMODEL(models.Model):
#
    P_User                   = models.OneToOneField(User               , on_delete=models.CASCADE   , blank=False  , null=False  , verbose_name="اسم المشترك")
    slug                     = models.SlugField(unique=False                     , db_index=True , blank=True  , null=False , verbose_name="الإسم التعريفي")
    P_FirstName              = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="الإسم الأول")
    P_FatherName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الاب")
    P_GrandFatherName        = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الجد")
    P_FamilyName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم العائلة")
    P_Photo                  = models.ImageField(upload_to='PersonaFile_Photo/'  , db_index=True , blank=False , null=False , verbose_name="الصورة الشخصية"      ,default='Default_Image.png')
    # P_Mobile                 = PhoneNumberField(                                   db_index=True , blank=False , null=False , verbose_name="الجوال")
    # P_Mobile                 = PhoneNumberField(unique=True                      , db_index=True , blank=False , null=False , verbose_name="الجوال")
    P_Mobile                 = PhoneNumberField(                                   db_index=True , blank=False , null=False , verbose_name="الجوال"              , default='+966555555555')
    P_Address                = models.CharField(max_length=100                   , db_index=True , blank=False , null=False ,verbose_name="العنوان")
    P_Notes                  = models.CharField(max_length=100                   , db_index=True , blank=True  , null=True  , verbose_name="الملاحظات"            , default='-')
#
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.P_User) 
    #
    def __str__(self):
        return f"{self.P_FirstName}, {self.P_FamilyName}"

    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['P_User']
    #
    class Meta:
        # The Name of the Model That Will Be Displayed In The Admin Page
        # verbose_name      = _('Personal')
        verbose_name_plural = 'Personal'
    #
    # 'admin'عرض الصورة في صفحة
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.P_Photo.url))  # 'admin'عرض حقل الصورة في صفحة
    image_tag.short_description='الصورة'  # 'admin'عرض إسم الصورة في صفحة
    #
    # 'admin'عرض إسم المستخدم رباعياً في صفحة
    def full_name(self):
        return str(self.P_FirstName + ' ' + self.P_FatherName + ' ' + self.P_GrandFatherName + ' ' + self.P_FamilyName)
    full_name.short_description='الإسم رباعيا'  # 'admin'عرض إسم الصورة في صفحة


#
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ
    def create_personal(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            PersonalsMODEL.objects.create(P_User=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(create_personal , sender=User)
    #
    
    # Auto Save Slug 
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.P_User)
        super(PersonalsMODEL , self).save(*args , **kwargs)
# #
    # def save(self , *args , **kwargs):
    #     if not self.P_Mobile:
    #         self.P_Mobile = str(966506361923)
    #     super(PersonalsMODEL , self).save(*args , **kwargs)





### (1) CREATE OTP **************************************************************************************************************
#
# # Create an OTP and send it to the e-mail (1)
# @receiver(post_save,sender=User)
# def Create_otp_send_it_to_email_after_registering_new_userDEF(sender,instance,created,**kwargs):
#         otp = ""
#         otp= f'{str(random.randint(1000,9999))}'
#         user = instance.email
#         SendTo = user
#         send_mail(
#         'Family Association - One Time Password', f'Your OTP pin is: {otp}', EMAIL_HOST_USER, [SendTo],
#         fail_silently=False,)
#         return otp
# #
# # Create an OTP and send it to the Whatsapp (2)
# @receiver(post_save,sender=User)
# def Create_otp_send_it_to_whatsapp_after_Registering_new_userDEF(sender,instance,created,**kwargs):
#     otp = ""
#     otp= f'{str(random.randint(1000,9999))}'

#     Phone = '+966506361923'
#     # Phone = '+966567677895'
#     Message=f'Your OTP pin is: {otp}'
#     webbrowser.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
#     time.sleep(10)
#     pyautogui.press('enter')

### (2) SEND EMAIL *****************************************************************************************************************
#
# # Send Email After Registering New User (1)
# @receiver(post_save,sender=User)
# def send_email_after_registering_new_user(sender,instance,created,**kwargs):
#     user = instance.email
#     SendTo = user
#     send_mail(
#             'Family Association',
#             'User Account Created - We Thank You and welcome you to join us.',
#             EMAIL_HOST_USER,
#             [SendTo],
#             fail_silently=False,)
# #
# # Send Email After Deleted User Account (2)
# @receiver(post_delete,sender=User)
# def Send_email_after_deleting_user(sender,instance,*args,**kwargs):
#     user = instance.email
#     SendTo = user
#     send_mail(
#             'Family Association',
#             'User Account Deleted - We wish you a nice day',
#             EMAIL_HOST_USER,
#             [SendTo],
#             fail_silently=False,)
#
### (3) SEND WHATSAPP *****************************************************************************************************************
# #
# # Send Message To Whatsapp After Registering New User (1)
# @receiver(post_save,sender=User)
# def send_message_to_whatsapp_after_registering_new_user(sender,instance,created,**kwargs):
#     Phone = '+966506361923'
#     # Phone = '+966567677895'
#     Message='User Account Created - We Thank You and welcome you to join us.'
#     webbrowser.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
#     time.sleep(10)
#     pyautogui.press('enter')
# #
# # Send Message To Whatsapp After Deleting User Account (2)
# @receiver(post_delete,sender=User)
# def Send_message_to_whatsapp_after_deleting_user(sender,instance,*args,**kwargs):
#     Phone = '+966506361923'
#     # Phone = '+966567677895'
#     Message='User Account Deleted - We wish you a nice day'
#     webbrowser.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
#     time.sleep(10)
#     pyautogui.press('enter')
#**************************************************************************************************************************************

    # """Send a Congratulatory Email For Joining Us
    #    Send an Email After Registering a User
    # """
    # def send_email_after_registering_user(self , *args , **kwargs):
    #     user = User.objects.get(id=self.P_User.pk)
    #     SendTo = user.email
    #     print(SendTo)
    #     send_mail(
    #         'Family Association',
    #         'We Thank You and welcome you to join us',
    #         EMAIL_HOST_USER,
    #         [SendTo],
    #         fail_silently=False,
    #     )


# """Whatsapp Using Twilio
# Send a Congratulatory Whatsapp For Joining Us
# Send an Whatsapp After Deleted User Account
# """
# @receiver(post_save,sender=User)
# def send_message_to_whatsapp_with_twilio(sender,instance,created,**kwargs):
#     # [TWILIO_ACCOUNT_SID]Account SID From Twilio
#     account_sid = 'AC65eae2f82119281192dd22599087fa05'
#     # [TWILIO_AUTH_TOKEN]Auth Token From Twilio            
#     auth_token  = 'cafab142d89f0ab765ddd5cc96504b5c' 
#     client      = Client(account_sid, auth_token)
#     message     = client.messages.create(media_url=["https://duckduckgo.com/?q=flor.png&atb=v329-1&iar=images&iax=images&ia=images&iai=https%3A%2F%2Fwww.pngpix.com%2Fwp-content%2Fuploads%2F2016%2F03%2FDahlia-Flower-PNG-image.png"], from_='whatsapp:+19377875117', body="Family Associatior - Hi there The Curent Result Is - ", to='whatsapp:+966506361923')
#     print('Twilio - message Whatsapp Sended',message)

# (2) Financial Statements``
class  FinancialStatementsMODEL(models.Model):
    #
    FS_User                    = models.OneToOneField(User      , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    FS_SubscriptionAmount      = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="مبلغ الإشتراك")
    FS_NumberPaymentsDue       = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الدفعات")
    FS_BankName                = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم البنك")
    FS_BankAccount             = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الحساب البنكي - الآيبان")
    FS_Notes                   = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات"                 , default='-')
    #
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.FS_User)
    #
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['FS_User']
#
    class Meta:
        # The Name of the Model That Will Be Displayed In The Admin Page
        verbose_name_plural = 'Financial Statements'

# #
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ
    def create_financial_statements(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            FinancialStatementsMODEL.objects.create(FS_User=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(create_financial_statements , sender=User)
#######################################################
# (3)Comprehensive Record
class  DatesReceivingMoneyPaymentsMODEL(models.Model):
    # Variable To Save The Number Of Months
    CHOOSE_MONTH_NUMBER = '00'
    JAN                 = '01'
    FEB                 = '02'
    MAR                 = '03'
    APR                 = '04'
    MAY                 = '05'
    JUN                 = '06'
    JUL                 = '07'
    AUG                 = '08'
    SEP                 = '09'
    OCT                 = '10'
    NOV                 = '11'
    DEC                 = '12'
    #
    # The Number Of Months
    MONTH_NUMBER = [
    (CHOOSE_MONTH_NUMBER ,  'Choose The Month Number'),
    (JAN                 ,                       '01'),
    (FEB                 ,                       '02'),
    (MAR                 ,                       '03'),
    (APR                 ,                       '04'),
    (MAY                 ,                       '05'),
    (JUN                 ,                       '06'),
    (JUL                 ,                       '07'),
    (AUG                 ,                       '08'),
    (SEP                 ,                       '09'),
    (OCT                 ,                       '10'),
    (NOV                 ,                       '11'),
    (DEC                 ,                       '12'),
    ]
    #
    #
    # Variable To Save The Month Code
    # The Data Will be Saved in the Database
    JANUARY             = '01-January__Jumada Al-Awwal-(05)  '
    FEBRUARY            = '02-February_Jumada Al-Thani-(06)  '
    MARCH               = '03-March______________Rajab-(07)  '
    APRIL               = '04-April_____________Shaban-(08)  '
    MAY                 = '05-May______________Ramadan-(09)  ' 
    JUNE                = '06-June_____________Shawwal-(10)  '
    JULY                = '07-July__________Dhul-Qadah-(11)  '
    AUGUST              = '08-August_______Dhul-Hijjah-(12)  '
    SEPTEMBER           = '09-September_______Muharram-(01)  '
    OCTOBER             = '10-October____________Safar-(02)  '
    NOVEMBER            = '11-November___Rabi Al-Awwal-(03)  '
    DECEMBER            = '12-December___Rabi Al-Thani-(04)  '
    NO                  = 'The Date Has Not Yet Been Set-(00)'
    #
    # List Of The Names Of The Months
    # This Data Will Be shown In the Menu
    MONTH_NAME = [
    (JANUARY            ,  '01-January      (05)  جمادى الأولى')      ,
    (FEBRUARY           ,  '02-February     جمادى الثاني  (06)')      ,
    (MARCH              ,  '03-March        رجب           (07)')      ,
    (APRIL              ,  '04-April        شعبان         (08)')      ,
    (MAY                ,  '05-May          رمضان         (09)')      ,
    (JUNE               ,  '06-June         شوال          (10)')      ,
    (JULY               ,  '07-July         ذو القعدة     (11)')      ,
    (AUGUST             ,  '08-August       ذو الحجة      (12)')      ,
    (SEPTEMBER          ,  '09-September    محرم          (01)')      ,
    (OCTOBER            ,  '10-October      صفر           (02)')      ,
    (NOVEMBER           ,  '11-November     ربيع الأول    (03)')      ,
    (DECEMBER           ,  '12-December     ربيع الثاني   (04)')      ,
    (NO                 ,  'لم يتم تحديد اي رغبة حتى الأن-(00)') ,
    ]
    
    #
    #
    DRMP_User                              = models.ForeignKey(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    DRMP_DateReceivingMoneyPayments_Long   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="موعد إستلام المال - بالشهر"     , choices=MONTH_NAME , default=NO          , help_text='Required Field')
    DRMP_DateReceivingMoneyPayments_Short  = models.DateField(                                                   db_index=True , blank=True   , null=True   , verbose_name="موعد إستلام المال - بالتاريخ"                         ,default=date.today   , help_text='Required Field')
    DRMP_Notes                             = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات"                                           , default='-')
    # Display The Name Of This Field In The Admin Page
    def __str__(self):
        return str(self.DRMP_DateReceivingMoneyPayments_Long)
    #
    # Arrange The Fields In Ascending Order 'Z-A'
    class Meta:
        ordering = ['DRMP_DateReceivingMoneyPayments_Short']
    class Meta:
        # The Name of the Model That Will Be Displayed In The Admin Page
        verbose_name_plural = 'Dates Receiving Money Payments'

#
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ
    def create_dates_receiving_money_payments(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            DatesReceivingMoneyPaymentsMODEL.objects.create(DRMP_User=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(create_dates_receiving_money_payments , sender=User)

#
# (3)Comprehensive Record
class  SubscribersDesiresMODEL(models.Model):
    # Variable To Save The Number Of Months
    CHOOSE_MONTH_NUMBER = '00'
    JAN                 = '01'
    FEB                 = '02'
    MAR                 = '03'
    APR                 = '04'
    MAY                 = '05'
    JUN                 = '06'
    JUL                 = '07'
    AUG                 = '08'
    SEP                 = '09'
    OCT                 = '10'
    NOV                 = '11'
    DEC                 = '12'
    #
    # The Number Of Months
    MONTH_NUMBER = [
    (CHOOSE_MONTH_NUMBER ,  'Choose The Month Number'),
    (JAN                 ,                       '01'),
    (FEB                 ,                       '02'),
    (MAR                 ,                       '03'),
    (APR                 ,                       '04'),
    (MAY                 ,                       '05'),
    (JUN                 ,                       '06'),
    (JUL                 ,                       '07'),
    (AUG                 ,                       '08'),
    (SEP                 ,                       '09'),
    (OCT                 ,                       '10'),
    (NOV                 ,                       '11'),
    (DEC                 ,                       '12'),
    ]
    #
    #
    # Variable To Save The Month Code
    # The Data Will be Saved in the Database
    JANUARY             = '01-January____جمادى الأولى-(05)   '
    FEBRUARY            = '02-February___جمادى الثاني-(06)   '
    MARCH               = '03-March______راجب-(07)           '
    APRIL               = '04-April______شعبان-(08)          '
    MAY                 = '05-May________رمضان-(09)          ' 
    JUNE                = '06-June_______شوال-(10)           '
    JULY                = '07-July_______ذو القعدة-(11)      '
    AUGUST              = '08-August_____ذو الحجة-(12)       '
    SEPTEMBER           = '09-September__محرم-(01)           '
    OCTOBER             = '10-October____صفر-(02)            '
    NOVEMBER            = '11-November___ربيع الأول-(03)     '
    DECEMBER            = '12-December___ربيع الثاني-(04)    '
    NO                  = 'لم يتم تحديد اي رغبة حتى الأن-(00)'
    #
    # List Of The Names Of The Months
    # This Data Will Be shown In the Menu
    MONTH_NAME = [
    (JANUARY            ,  '01-January      (05)  جمادى الأولى')      ,
    (FEBRUARY           ,  '02-February     جمادى الثاني  (06)')      ,
    (MARCH              ,  '03-March        رجب           (07)')      ,
    (APRIL              ,  '04-April        شعبان         (08)')      ,
    (MAY                ,  '05-May          رمضان         (09)')      ,
    (JUNE               ,  '06-June         شوال          (10)')      ,
    (JULY               ,  '07-July         ذو القعدة     (11)')      ,
    (AUGUST             ,  '08-August       ذو الحجة      (12)')      ,
    (SEPTEMBER          ,  '09-September    محرم          (01)')      ,
    (OCTOBER            ,  '10-October      صفر           (02)')      ,
    (NOVEMBER           ,  '11-November     ربيع الأول    (03)')      ,
    (DECEMBER           ,  '12-December     ربيع الثاني   (04)')      ,
    (NO                 ,  'لم يتم تحديد اي رغبة حتى الأن-(00)') ,
    ]
    #
    #
    SD_User           = models.OneToOneField(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    # SD_Desire   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الرغبة"     , choices=MONTH_NAME , default=NO , help_text='Required Field')
    SD_Desire_first   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الرغبة الأولى"     , choices=MONTH_NAME , default=NO , help_text='Required Field')
    SD_Desire_second  = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الرغبة الثانية"    , choices=MONTH_NAME , default=NO , help_text='Required Field')
    SD_Desire_third   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الرغبة الثالثة"    , choices=MONTH_NAME , default=NO , help_text='Required Field')
    SD_Notes                             = models.CharField(max_length=100                 , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات"                               , default='-')
    # Display The Name Of This Field In The Admin Page
    def __str__(self):
        return str(self.SD_Desire_first)
    #
    # Arrange The Fields In Ascending Order 'Z-A'
    class Meta:
        ordering = ['SD_Desire_first']
    class Meta:
        # The Name of the Model That Will Be Displayed In The Admin Page
        verbose_name_plural = 'Subscribers Desires'

#
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ
    def create_subscribers_desires(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            SubscribersDesiresMODEL.objects.create(SD_User=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(create_subscribers_desires , sender=User)







# (4) Dues Record
# class  DuesRecordMODEL(models.Model):
#     #
#         # Variable To Save The Month Code
#     # The Data Will be Saved in the Database
#     JANUARY             = '01-January__Jumada Al-Awwal-(05)  '
#     FEBRUARY            = '02-February_Jumada Al-Thani-(06)  '
#     MARCH               = '03-March______________Rajab-(07)  '
#     APRIL               = '04-April_____________Shaban-(08)  '
#     MAY                 = '05-May______________Ramadan-(09)  ' 
#     JUNE                = '06-June_____________Shawwal-(10)  '
#     JULY                = '07-July__________Dhul-Qadah-(11)  '
#     AUGUST              = '08-August_______Dhul-Hijjah-(12)  '
#     SEPTEMBER           = '09-September_______Muharram-(01)  '
#     OCTOBER             = '10-October____________Safar-(02)  '
#     NOVEMBER            = '11-November___Rabi Al-Awwal-(03)  '
#     DECEMBER            = '12-December___Rabi Al-Thani-(04)  '
#     NO                  = 'The Date Has Not Yet Been Set-(00)'
#     #
#     # List Of The Names Of The Months
#     # This Data Will Be shown In the Menu
#     MONTH_NAME = [
#     (JANUARY            ,  '01-January__Jumada Al-Awwal-(05)')   ,
#     (FEBRUARY           ,  '02-February_Jumada Al-Thani-(06)')   ,
#     (MARCH              ,  '03-March______________Rajab-(07)')   ,
#     (APRIL              ,  '04-April_____________Shaban-(08)')   ,
#     (MAY                ,  '05-May______________Ramadan-(09)')   ,
#     (JUNE               ,  '06-June_____________Shawwal-(10)')   ,
#     (JULY               ,  '07-July__________Dhul-Qadah-(11)')   ,
#     (AUGUST             ,  '08-August_______Dhul-Hijjah-(12)')   ,
#     (SEPTEMBER          ,  '09-September_______Muharram-(01)')   ,
#     (OCTOBER            ,  '10-October____________Safar-(02)')   ,
#     (NOVEMBER           ,  '11-November___Rabi Al-Awwal-(03)')   ,
#     (DECEMBER           ,  '12-December___Rabi Al-Thani-(04)')   ,
#     (NO                 ,  'The Date Has Not Yet Been Set-(00)') ,
#     ]
#     #
#     #
#     DRMP_User                              = models.ForeignKey(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
#     DRMP_DateReceivingMoneyPayments_Long   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="موعد إستلام المال - بالشهر"     , choices=MONTH_NAME , default=NO , help_text='Required Field')
#     DRMP_DateReceivingMoneyPayments_Short  = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="موعد إستلام المال - بالتاريخ"                                     , help_text='Required Field')
#     DRMP_Notes                             = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")
#     FS_SubscriptionAmount                  = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="مبلغ الإشتراك")
#     FS_NumberPaymentsDue                   = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الدفعات")
#     P_FirstName                            = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الإسم الأول")
#     P_FatherName                           = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم الاب")
#     P_GrandFatherName                      = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم الجد")
#     P_FamilyName                           = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم العائلة")

# class Profile(models.Model):
#     user   = models.OneToOneField(User , on_delete=models.CASCADE)
#     mobile = models.IntegerField(blank=True , null=True )

# class Profile(models.Model):
#     user   = models.OneToOneField(User, on_delete=models.CASCADE)
#     # mobile = models.IntegerField(blank=True  , null=True)
#     # mobile  = models.IntegerField(blank=True , null=False, default=966506361923)
#     mobile = models.IntegerField(blank=True , default=966111111111)

    
    # def create_Profile(sender, **kwargs):
    #     if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
    #         Profile.objects.create(user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    # post_save.connect(create_Profile , sender=User)

