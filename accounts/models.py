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
from django.core.mail import send_mail
# from django.core.mail import send_mail
from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS

####################################
# (1)Personal Data
class PersonalsMODEL(models.Model):
#
    P_User                   = models.OneToOneField(User                         , on_delete=models.CASCADE                 , verbose_name="اسم المشترك")
    P_Avialable              = models.BooleanField(default=True                  , db_index=True , blank=False , null=False , verbose_name="حالة المشترك_نشط")
    slug                     = models.SlugField(unique=False                     , db_index=True , blank=True  , null=False , verbose_name="الإسم التعريفي")
    P_FirstName              = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="الإسم الأول")
    P_FatherName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الاب")
    P_GrandFatherName        = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الجد")
    P_FamilyName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم العائلة")
    P_Photo                  = models.ImageField(upload_to='PersonaFile_Photo/'  , db_index=True , blank=False , null=False , verbose_name="الصورة الشخصية"      ,default='Default_Image.png')
    P_Mobile                 = models.CharField(max_length=10                    , db_index=True , blank=False , null=False , verbose_name="الجوال")
    P_Address                = models.CharField(max_length=100                   , db_index=True , blank=False , null=False ,verbose_name="العنوان")
    P_Notes                  = models.CharField(max_length=100                   , db_index=True , blank=True  , null=True  , verbose_name="الملاحظات")
#
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.P_User)
    #
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['P_User']
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
            self.slug = slugify(self.P_User.username)
        super(PersonalsMODEL , self).save(*args , **kwargs)
    #
    """Send a Congratulatory Email For Joining Us
       Send an Email After Registering a User
    """
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
#   
##
"""
Send a Congratulatory Email For Joining Us
Send an Email After Registering a User
"""
@receiver(post_save,sender=User)
def send_email_after_registering_user(sender,instance,created,**kwargs):
    user = instance.email
    SendTo = user
    send_mail(
            'Family Association',
            'User Profile Created - We Thank You and welcome you to join us.',
            EMAIL_HOST_USER,
            [SendTo],
            fail_silently=False,
        )
##
"""
Send a Congratulatory Email For Joining Us
Send an Email After Registering a User
"""
@receiver(post_delete,sender=User)
def Send_email_after_deleting_user(sender,instance,*args,**kwargs):
    user = instance.email
    SendTo = user
    send_mail(
            'Family Association',
            'User Profile Deleted - We wish you a nice day',
            EMAIL_HOST_USER,
            [SendTo],
            fail_silently=False,
        )
##
# (2) Financial Statements``
class  FinancialStatementsMODEL(models.Model):
    #
    FS_User                    = models.OneToOneField(User      , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    FS_SubscriptionAmount      = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="مبلغ الإشتراك")
    FS_NumberPaymentsDue       = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الدفعات")
    FS_BankName                = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم البنك")
    FS_BankAccount             = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الحساب البنكي - الآيبان")
    FS_Notes                   = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")
    #
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.FS_User)
    #
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['FS_User']
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
    (JANUARY            ,  '01-January__Jumada Al-Awwal-(05)')   ,
    (FEBRUARY           ,  '02-February_Jumada Al-Thani-(06)')   ,
    (MARCH              ,  '03-March______________Rajab-(07)')   ,
    (APRIL              ,  '04-April_____________Shaban-(08)')   ,
    (MAY                ,  '05-May______________Ramadan-(09)')   ,
    (JUNE               ,  '06-June_____________Shawwal-(10)')   ,
    (JULY               ,  '07-July__________Dhul-Qadah-(11)')   ,
    (AUGUST             ,  '08-August_______Dhul-Hijjah-(12)')   ,
    (SEPTEMBER          ,  '09-September_______Muharram-(01)')   ,
    (OCTOBER            ,  '10-October____________Safar-(02)')   ,
    (NOVEMBER           ,  '11-November___Rabi Al-Awwal-(03)')   ,
    (DECEMBER           ,  '12-December___Rabi Al-Thani-(04)')   ,
    (NO                 ,  'The Date Has Not Yet Been Set-(00)') ,
    ]
    #
    #
    DRMP_User                              = models.ForeignKey(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    DRMP_DateReceivingMoneyPayments_Long   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="موعد إستلام المال - بالشهر"     , choices=MONTH_NAME , default=NO , help_text='Required Field')
    DRMP_DateReceivingMoneyPayments_Short  = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="موعد إستلام المال - بالتاريخ"                                     , help_text='Required Field')
    DRMP_Notes                             = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")
    # Display The Name Of This Field In The Admin Page
    def __str__(self):
        return str(self.DRMP_DateReceivingMoneyPayments_Long)
    #
    # Arrange The Fields In Ascending Order 'Z-A'
    class Meta:
        ordering = ['DRMP_DateReceivingMoneyPayments_Short']
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
###############################################  
# (4) Dues Record
class  DuesRecordMODEL(models.Model):
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
    (JANUARY            ,  '01-January__Jumada Al-Awwal-(05)')   ,
    (FEBRUARY           ,  '02-February_Jumada Al-Thani-(06)')   ,
    (MARCH              ,  '03-March______________Rajab-(07)')   ,
    (APRIL              ,  '04-April_____________Shaban-(08)')   ,
    (MAY                ,  '05-May______________Ramadan-(09)')   ,
    (JUNE               ,  '06-June_____________Shawwal-(10)')   ,
    (JULY               ,  '07-July__________Dhul-Qadah-(11)')   ,
    (AUGUST             ,  '08-August_______Dhul-Hijjah-(12)')   ,
    (SEPTEMBER          ,  '09-September_______Muharram-(01)')   ,
    (OCTOBER            ,  '10-October____________Safar-(02)')   ,
    (NOVEMBER           ,  '11-November___Rabi Al-Awwal-(03)')   ,
    (DECEMBER           ,  '12-December___Rabi Al-Thani-(04)')   ,
    (NO                 ,  'The Date Has Not Yet Been Set-(00)') ,
    ]
    #
    #
    DRMP_User                              = models.ForeignKey(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    DRMP_DateReceivingMoneyPayments_Long   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="موعد إستلام المال - بالشهر"     , choices=MONTH_NAME , default=NO , help_text='Required Field')
    DRMP_DateReceivingMoneyPayments_Short  = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="موعد إستلام المال - بالتاريخ"                                     , help_text='Required Field')
    DRMP_Notes                             = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")
    FS_SubscriptionAmount                  = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="مبلغ الإشتراك")
    FS_NumberPaymentsDue                   = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الدفعات")
    P_FirstName                            = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الإسم الأول")
    P_FatherName                           = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم الاب")
    P_GrandFatherName                      = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم الجد")
    P_FamilyName                           = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم العائلة")

